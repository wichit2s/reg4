from rest_framework import routers
from . import views 

router = routers.DefaultRouter()
router.register(r'member',         views.MemberViewset)
router.register(r'note',           views.NoteViewset)
router.register(r'curriculum',     views.CurriculumViewset)
router.register(r'course',         views.CourseViewset)
router.register(r'student',        views.StudentViewset)

