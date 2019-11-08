from . import db


class Pets(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'pets'
    pet = db.Column(db.String(64),
                         index=False,
                         unique=False,
                         nullable=False)
    name = db.Column(db.String(255),
                     primary_key=True,
                      index=True,
                      unique=True,
                      nullable=False)
    color = db.Column(db.String(255),
                    index=False,
                    unique=False,
                    nullable=False)


    def __repr__(self):
        return 'name: {}, pet: {}, color: {}'.format(self.name, self.pet, self.color)