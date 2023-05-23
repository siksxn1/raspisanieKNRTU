class ILesson:
    lessonsName: str
    audence: str
    index: int
    day: int
    is_even: bool

    def __init__(self, lessonsName: str, audence: str, index: int, day: int, is_even: bool) -> None:
        self.lessonsName = lessonsName
        self.audence = audence
        self.index = index
        self.day = day
        self.is_even = is_even

class IDay:
    day_num: int
    lessons: list
    is_even: bool

    def __init__(self) -> None:
        self.lessons = []

    def add_lesson(self, lesson: ILesson):
        self.lessons.append(lesson)


class IWeek:
    is_even:bool
    days: list

    def add_lesson(self, lesson: ILesson):
        if not self.day_exists(lesson.day):
            self.days.append(IDay())

        for day in self.days:
            if day.day_num == lesson.day:
                day.add_lesson(lesson)

    def day_exists(self, num: int) -> bool:
        for day in self.days:
            if day.day_num == num:
                return True
            
        return False
    
    def __init__(self, is_even) -> None:
        self.is_even = is_even


class ITimeTable:
    weeks: list

    def add_lesson(self, lesson: ILesson):
        for week in self.weeks:
            if week.is_even == lesson.is_even:
                week.add_lesson(lesson)


    def __init__(self) -> None:
        self.weeks = []

        self.weeks.append(IWeek(True))
        self.weeks.append(IWeek(False))

