import csv

from board.models import Board
from common.models import ValueObject, Printer, Reader

#SET FOREIGN_KEY_CHECKS = 0;
#위에 코드는 도커에서 foreign 키에 대한 에러 발생시 사용하면 된다.
from user.models import User


class DbUploader():
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'board/data/'
        vo.fname = 'board.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        self.insert_board()
        print('##########  2  ##########')

    def insert_board(self):
        with open(self.csvfile, newline='', encoding='utf8') as csvfile:
            data_reader = csv.DictReader(csvfile)
            for row in data_reader:
                u = User()
                user = User.objects.all().filter(user_email=row['writen']).values()[0]
                # user = User.objects.all().values()[0]
                u.id = user['id']
                Board.objects.create(title=row['title'],
                                     body=row['body'],
                                     comment=row['comment'],
                                     writen=u,
                                     create_at=row['create_at'],
                                     update_at=row['update_at'])
            print('BOARD DATA UPLOADED SUCCESSFUIY! ')