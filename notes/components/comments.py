from django_unicorn.components import UnicornView
from ..models import Comments,Notes
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentsView(UnicornView):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)  
        self.noteID = kwargs.get("noteID")
    author: User = None
    note_ref : Notes = None
    comments: Comments = None
    comment: str = ""

    def mount(self):
        self.author = self.request.user
        self.note_ref = Notes.objects.get(id=self.noteID)
        self.comments = Comments.objects.filter(note =self.note_ref).order_by('-date')
        return super().mount()

    def submit(self):
        Comments.objects.create(
            author_id=self.author,
            note =self.note_ref,
            comment=self.comment
        )
        self.comment = ""
        self.comments = Comments.objects.filter(note=self.noteID).order_by('-date')
        print(self.comments)
        