from typing_extensions import Literal

class Collation:
    def __init__(
        self,
        locale: str,
        caseLevel: bool | None = ...,
        strength: Literal[1, 2, 3, 4, 5] | None = ...,
        numericOrdering: bool | None = ...,
        alternate: Literal["non-ignorable", "shifted"] | None = ...,
        maxVariable: Literal["punct", "space"] | None = ...,
        normalization: bool | None = ...,
        backwards: bool | None = ...,
    ) -> None: ...

class CollationStrength:
    PRIMARY: Literal[1]
    SECONDARY: Literal[2]
    TERTIARY: Literal[3]
    QUATERNARY: Literal[4]
    IDENTICAL: Literal[5]

class CollationAlternate:
    NON_IGNOREABLE: Literal["non-ignorable"]
    SHIFTED: Literal["shifted"]

class CollationMaxVariable:
    PUNCT: Literal["punct"]
    SPACE: Literal["space"]

class CollationCaseFirst:
    UPPER: Literal["upper"]
    LOWER: Literal["lower"]
    OFF: Literal["off"]
