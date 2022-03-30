"""Representations of courses in Canvas.

Courses are located on either the gu.instructure.com or
chalmers.instructure.com domain, or for shared courses, both.

A GU only course will have a "normal" Canvas ID and course code, for example:

* URL: https://gu.instructure.com/courses/21699
* Canvas ID: 21699
* Course code: DIT181

It seems like `canvas.gu.se` can also work as the domain.

Any course that is available to Chalmers will have a "normal" Canvas ID.
However, if it is a course that is shared with GU, this will be reflected in
the course code.  For example:

* URL: https://chalmers.instructure.com/courses/18287
* Canvas ID: 18287
* Course code: EDA343 / DIT423

In addition, there appears to exist "pseudo pages" on the GU domain for (some,
not all?) courses shared with Chalmers. The IDs on these pages are formatted in
a special way, with two ~5 digit numbers separated by a bunch of zeroes.  The
zeroes might also be formated as a tilde character (~) sometimes.  These
"pseudo pages" only seem to exist as redirections to the corresonding courses
on the Chalmers domain, which is the "canonical" page.  Using any navigation on
a pseudo page will direct to the corresponding Chalmers page.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Domain(Enum):
    GU = 'gu.instructure.com'
    CHALMERS = 'chalmers.instructure.com'


@dataclass(frozen=True)
class Course:
    """Representation of a Canvas course."""
    domain: Domain
    canvas_id: int
    name: str
    course_code: str
    pseudo_id: Optional[tuple[int, int]] = None

    def __repr__(self):
        return f'<Course {self.domain.name}/{self.canvas_id} "{self.course_code}">'

    def __str__(self):
        return self.course_code
