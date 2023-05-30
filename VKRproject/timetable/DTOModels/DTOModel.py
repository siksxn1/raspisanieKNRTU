import json
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

    def toJSON(self):
        return  {
            "lessonsName": self.lessonsName,
            "audence": self.audence,
            "index": self.index
        }

class IDay:
    day_num: int
    lessons: list
    is_even: bool

    def __init__(self, day_num: int) -> None:
        self.lessons = []
        self.day_num = day_num

    def add_lesson(self, lesson: ILesson):
        self.lessons.append(lesson)

    def toJSON(self):
        lessons = []
        for lesson in self.lessons:
            lessons.append((lesson.toJSON()))

        return {
            "lessons": lessons,
            "day_num": self.day_num
        }

class IWeek:
    is_even:bool
    days: list

    def add_lesson(self, lesson: ILesson):
        if not self.day_exists(lesson.day):
            self.days.append(IDay(lesson.day))

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
        self.days = []

    def toJSON(self):
        days = []

        for day in self.days:
            days.append(day.toJSON())

        return {
            "days": days,
            "is_even": self.is_even
        }


class ITimeTable:
    weeks: list

    def add_lesson(self, lesson: ILesson):
        for week in self.weeks:
            if week.is_even == lesson.is_even:
                week.add_lesson(lesson)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.dict,
                          sort_keys=True, indent=4)


    def __init__(self) -> None:
        self.weeks = []

        self.weeks.append(IWeek(True))
        self.weeks.append(IWeek(False))

    def toJSON(self):
        weeks = []

        for week in self.weeks:
            weeks.append(week.toJSON())

        return {
            "weeks": weeks
        }

