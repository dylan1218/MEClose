from .models import userReviewerMapping

class getReviewer:

    def __init__(self, user, entity):
        self.assignedUser = user
        self.assignedUserEntity = entity

    def get_reviewer(self):
        reviewerListMatch = userReviewerMapping.objects.all().filter(entity=self.assignedUserEntity, user=self.assignedUser)
        if reviewerListMatch.first() == None:
            return "No reviewer mapping found"
        else:
            return reviewerListMatch.first().userReviewer
    
    def get_reviewer_systemIdentifier(self):
        reviewerListMatch = userReviewerMapping.objects.all().filter(entity=self.assignedUserEntity, systemIdentifier=self.assignedUser)
        if reviewerListMatch.first() == None:
            return "No reviewer mapping found"
        else:
            return reviewerListMatch.first().userReviewer