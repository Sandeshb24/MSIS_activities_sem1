"""Assignment 2: Semantic tagging with GloVe and NumPy.
Usage: python semantic_tagging.py manipal.txt
"""
import re
import string
import sys

import numpy as np

from vector import Vector

TAGS = [
    "research", "innovation", "education", "university", "students",
    "faculty", "campus", "engineering", "medicine", "technology",
    "curriculum", "collaboration", "publication", "laboratory",
    "scholarship", "mentorship", "internship", "entrepreneurship",
    "accreditation", "alumni",
]  # all single-word; for multi-word use e.g. "higher education"

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "is", "are",
    "was", "were", "with", "at", "by", "from",
    # additions for LinkedIn text:
    "it", "this", "that", "these", "those", "our", "we", "you", "your", "they",
    "their", "his", "her", "its", "has", "have", "had", "will", "can", "be",
    "been", "as", "but", "not", "all", "more", "also", "about", "who", "which",
}


def load_model():
    import gensim.downloader as api
    return api.load("glove-wiki-gigaword-50")


def preprocess(text):
    """Returns (n_before, tokens_after_steps_1_to_5)."""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = text.split()
    n_before = len(tokens)
    tokens = [t for t in tokens if t not in STOPWORDS]
    tokens = [t for t in tokens if len(t) > 2]
    return n_before, tokens


def build_tag_matrix(model, tags):
    if len(tags) != 20:
        raise ValueError("Exactly 20 tags required")
    rows = []
    for tag in tags:
        words = tag.lower().split()
        for w in words:
            if w not in model.key_to_index:
                raise ValueError(f"Tag not in vocabulary: {w}")
        rows.append(np.mean([model[w] for w in words], axis=0))
    return list(tags), np.array(rows)


def build_text_matrix(model, tokens):
    in_vocab, oov = [], []
    for t in tokens:
        (in_vocab if t in model.key_to_index else oov).append(t)
    if in_vocab:
        W = np.array([model[t] for t in in_vocab])
    else:
        W = np.empty((0, 50))
    return in_vocab, oov, W


def similarity_matrix_vector_class(W, T):
    S = []
    for w in W:
        vw = Vector(w)
        S.append([vw.cosine_similarity(Vector(t)) for t in T])
    return np.array(S)


def similarity_matrix_numpy(W, T):
    W_norm = np.linalg.norm(W, axis=1, keepdims=True)
    T_norm = np.linalg.norm(T, axis=1, keepdims=True)
    if np.any(W_norm == 0) or np.any(T_norm == 0):
        raise ValueError("Zero-norm row encountered")
    return (W / W_norm) @ (T / T_norm).T


def rank_tags(tag_names, S, in_vocab_tokens):
    best_idx = np.argmax(S, axis=0)
    scores = S[best_idx, np.arange(S.shape[1])]
    order = np.argsort(-scores)
    return [(tag_names[j], float(scores[j]), in_vocab_tokens[best_idx[j]])
            for j in order]


def main(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    model = load_model()

    n_before, tokens = preprocess(text)
    in_vocab, oov, W = build_text_matrix(model, tokens)
    print(f"Tokens before preprocessing : {n_before}")
    print(f"Tokens after preprocessing  : {len(tokens)}")
    print(f"In-vocabulary tokens        : {len(in_vocab)}")
    print(f"Out-of-vocabulary tokens    : {len(oov)}")
    print(f"Distinct OOV tokens         : {sorted(set(oov))}")

    tag_names, T = build_tag_matrix(model, TAGS)
    print("T.shape =", T.shape)
    print("W.shape =", W.shape)
    if len(in_vocab) == 0:
        sys.exit("Error: no in-vocabulary words in the input text.")

    S_vec = similarity_matrix_vector_class(W, T)
    S_np = similarity_matrix_numpy(W, T)
    print("np.allclose:", np.allclose(S_vec, S_np, atol=1e-8))
    print("Max abs diff:", np.max(np.abs(S_vec - S_np)))

    ranking = rank_tags(tag_names, S_np, in_vocab)[:8]
    print(f"\n{'Rank':<6}{'Tag':<20}{'Score':<9}{'Best word':<18}Match")
    print("-" * 66)
    for r, (tag, score, word) in enumerate(ranking, 1):
        kind = "identical" if word == tag else "different"
        print(f"{r:<6}{tag:<20}{score:<9.3f}{word:<18}{kind}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "manipal.txt")
