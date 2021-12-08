import dropbox

class TransferData:
    def __init__(self, access_token) :
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files.upload(f.read(), file_to)

def main():
    access_token: 'sl.A9xhKGQ0xbne_xlttEWjjWSsWIzQIXS-cVFmVfiFVyFUeREc6ZzGuFV1C-qBzKA-uWn8gZHntgpoRJ5ode8lw7YE9axK8mrhvAiivX0HDt9xknXwPG01YCdMRDKB-MvwwjIDLRk'
    transferData = TransferData(access_token)

    file_from = input("Enter the name of the file from: ")
    file_to = input("Enter the name of the file to: ")

    # API v2
    transferData.upload_file(file_from, file_to)

    print("File has been moved")

main()
