
import math
from collections import Counter


def calculate_entropy(labels: list) -> float:
    """Calculate the entropy of a list of labels."""
    if not labels:
        return 0.0

    counts = Counter(labels)
    n = len(labels)

    return -sum(
        (count / n) * math.log2(count / n)
        for count in counts.values()
    )


def calculate_information_gain(
    examples: list[dict], attr: str, target_attr: str
) -> float:
    """Calculate the information gain of splitting on attr."""
    parent_entropy = calculate_entropy(
        [example[target_attr] for example in examples]
    )

    n = len(examples)
    weighted_entropy = 0.0

    # Sorted order ensures deterministic processing
    for value in sorted({example[attr] for example in examples}):
        subset = [
            example for example in examples
            if example[attr] == value
        ]

        weighted_entropy += (
            len(subset) / n
        ) * calculate_entropy(
            [example[target_attr] for example in subset]
        )

    return parent_entropy - weighted_entropy


def majority_class(examples: list[dict], target_attr: str) -> str:
    """Return the majority class. Break ties alphabetically."""
    counts = Counter(example[target_attr] for example in examples)
    max_count = max(counts.values())

    return min(
        label for label, count in counts.items()
        if count == max_count
    )


def learn_decision_tree(
    examples: list[dict],
    attributes: list[str],
    target_attr: str
) -> dict | str:
    """Build a decision tree using the ID3 algorithm."""

    # Handle empty examples defensively
    if not examples:
        return {}

    labels = [example[target_attr] for example in examples]

    # Case 1: All examples belong to the same class
    if len(set(labels)) == 1:
        return labels[0]

    # Case 2: No attributes remain; return majority class
    if not attributes:
        return majority_class(examples, target_attr)

    # Case 3: Select attribute with maximum information gain.
    # Strict > preserves the first attribute in a tie.
    best_attr = attributes[0]
    best_gain = calculate_information_gain(
        examples, best_attr, target_attr
    )

    for attr in attributes[1:]:
        gain = calculate_information_gain(
            examples, attr, target_attr
        )

        if gain > best_gain:
            best_gain = gain
            best_attr = attr

    tree = {best_attr: {}}
    remaining_attributes = [
        attr for attr in attributes if attr != best_attr
    ]

    # Process attribute values in sorted order
    values = sorted({example[best_attr] for example in examples})

    for value in values:
        subset = [
            example for example in examples
            if example[best_attr] == value
        ]

        tree[best_attr][value] = learn_decision_tree(
            subset, remaining_attributes, target_attr
        )

    return tree
