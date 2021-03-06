# coding=utf-8
import socket
from os.path import splitext
from HttpParser import HttpMassageParser
from resource import Resource


# return the content type of the response according to the file_extension.
def get_content_type(file_path):
    file_name, file_extension = splitext(file_path)
    return {
        '.jpg': 'image/jpg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.woff': 'application/x-font-woff',
        '.ttf': 'application/x-font-ttf',
        '.svg': 'image/svg+xml',
        '.eot': 'application/vnd.ms-fontobject',
        '.otf': 'application/x-font-otf',
        '.css': 'text/css',
        '.html': 'text/html',
        '.js': 'application/javascript',

    }.get(file_extension, 'text/html')


# create the resources table of the articles.
def create_resources_table():
    resources_list = [Resource('http://www.ynet.co.il/articles/0,7340,L-4713571,00.html',
                               'https://images1.ynet.co.il/PicServer4/2014/08/05/5506384/52203970100690640360no.jpg',
                               'החוש הדומיננטי שיעזור לכם בלימודים',
                               'החוש הדומיננטי שיעזור לכם בלימודים. אילו טיפים של שימושבחושים יעזרו לכם?'),
                      Resource('http://www.ynet.co.il/articles/0,7340,L-5045541,00.html',
                               'https://images1.ynet.co.il/PicServer5/2017/11/23/8172884/817287001000100980704no.jpg',
                               '"כ"ט בנובמבר: "שמחה שנמשכה ימים ולילות, הייתה אופוריה"',
                               'ב1947- הם היו ילדים או צעירים בתחילת דרכם,' +
                               ' אבל את היום הגורלי ב29- בנובמבר הם לא שוכחים עד היום.' +
                               ' "כולם היו צמודים לרדיו. אני זוכרת את התפרצות השמחה, ריקודים והתחבקויות."'),
                      Resource('https://www.calcalist.co.il/world/articles/0,7340,L-3726321,00.html',
                               'https://images1.calcalist.co.il/PicServer3/2017/11/30/775736/2_l.jpg',
                               'רוצים נייר טואלט? הזדהו: כך משפרים הסינים את מצב השירותים הציבוריים',
                               'שבוע קרא נשיא סין שי ג‘ינפינג להמשיך את מהפכת השירותים' +
                               ' הציבוריים עליה הכריז ב-2015. עד כה שופצו ונבנו 68 אלף מתקנים'),
                      Resource('http://www.nrg.co.il/online/13/ART2/902/962.html',
                               'http://www.nrg.co.il/images/archive/465x349/1/646/416.jpg',
                               'מחקו לכם הודעה בווטסאפ? עדיין תוכלו לקרוא אותה',
                               'אפליקציה בשם Notification History מאפשרת למשתמשי אנדרואיד' +
                               ' לקורא את הנתונים הזמניים הנשמרים ביומן הפעילות של הסמארטפון. כולל הודעות מחוקות.'),
                      Resource('http://www.nrg.co.il/online/55/ART2/904/542.html',
                               'http://www.nrg.co.il/images/archive/465x349/1/795/429.jpg',
                               'גם בחורף: זה בדיוק הזמן לקפוץ לאילת',
                               'העיר הדרומית נעימה לנופש גם בחודשי החורף.' +
                               ' כעת מוצעים מחירים אטרקטיביים במיוחד בחבילות שכוללות מגוון אטרקציות, לינה וטיסות'),
                      Resource('https://food.walla.co.il/item/3113079',
                               'https://img.wcdn.co.il/f_auto,w_700/2/5/1/3/2513314-46.jpg',
                               '12 בתי קפה שמתאימים לעבודה עם לפטופ',
                               'בין אם אתם סטודנטים או עצמאיים, זה תמיד סיפור למצוא בית קפה נעים וטעים לרבוץ בו.' +
                               ' קיבצנו עבורכם 12 מקומות אהובים בדיוק למטרה זו, בארבע הערים הגדולות'),
                      Resource('https://news.walla.co.il/item/3114145',
                               'https://img.wcdn.co.il/f_auto,w_700/2/4/9/5/2495334-46.jpg',
                               'שותק על אזריה, נלחם באהוד ברק: בנט מנסה להיבנות כימין ממלכתי',
                               'כשרגב נלחמת ברעש בתאטרון יפו, בנט משנה בשקט את נהלי סל התרבות כך ' +
                               'שהחומרים "השמאלנים" ייפלטו. כשהקשת הפוליטית מתרעמת על דיווחי' +
                               ' ה"דיל" של טראמפ עם הפלסטינים, בנט שותק עד שהרשות תסרב.'),
                      Resource('https://news.walla.co.il/item/3114283',
                               'https://img.wcdn.co.il/f_auto,w_700/2/5/1/4/2514588-46.jpg',
                               'רצח בכל שלושה ימים: צרפת יוצאת למאבק באלימות נגד נשים',
                               'אחרי ש126- נשים נרצחו בידי בני זוגן בשנה שעברה, ' +
                               'הציג מקרון צעדים חדשים למלחמה בתופעה. "זאת בושה לצרפת,"' +
                               ' אמר הנשיא שאחת מהבטחות הבחירות שלו הייתה להשיג שוויון מגדרי.')]
    return resources_list


# create the template page according to the number of articles.
def create_template_page(number_of_articles):
    data = open('files/template.html', 'rb').read()
    if number_of_articles == 0:
        return data

    if number_of_articles > len(resources_table):
        number_of_articles = len(resources_table)

    start = '<section id="feature" >'
    end = '</section><!--/#feature-->'
    start_row = '<div class="row">'
    end_row = '</div><!--/.row-->'
    header, _, rest = data.partition(start)
    result, _, footer = rest.partition(end)
    part1, _, rest2 = result.partition(start_row)
    template, _, part2 = rest2.partition(end_row)

    template = start_row + template + end_row
    dynamic = ''
    for i in range(0, number_of_articles):
        resource = resources_table[i]
        dynamic += template.replace('Title', resource.title).replace('link', resource.link) \
            .replace('Content', resource.content) \
            .replace('img src=""', 'img src="' + resource.image + '"')

    new_template = header + start + part1 + dynamic + part2 + end + footer
    return new_template


# create the response of the dynamic request
def dynamic_request(args):
    number_of_articles = 0
    if args != '':
        number_of_articles = int(args.split('=')[1])
    return create_template_page(number_of_articles)


# create the a http response according to the request.
def get_response(massageHttp):
    if 'If-Modified-Since' in massageHttp:  # case the resource is on the client cache.
        massage_parser = HttpMassageParser(1.1, 304, 'text/html', 'close', '')
        return massage_parser.get_massage()

    lines = massageHttp.splitlines()
    request = lines[0].split("GET /")[1].split(" HTTP/1.1")[0]
    if '?' in request:
        data_path, args = request.split('?')
    else:
        data_path = request
        args = ''

    if data_path.startswith('homepage'):  # dynamic request
        data = dynamic_request(args)
        massage_parser = HttpMassageParser(1.1, 200, 'text/html', 'close', data)
        return massage_parser.get_massage()

    # static request
    try:
        file_resource = open(data_path, 'rb')
    except IOError:
        try:
            file_resource = open('files/' + data_path, 'rb')

        except IOError:  # error - not found
            massage_parser = HttpMassageParser(1.1, 404, 'text/html', 'close', '')
            return massage_parser.get_massage()

    # found - create a 200 massage.
    data = file_resource.read()
    file_resource.close()
    massage_parser = HttpMassageParser(1.1, 200, get_content_type(data_path), 'close', data)
    return massage_parser.get_massage()


# initial server's tcp socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'
server_port = 80
server.bind((server_ip, server_port))
server.listen(5)
resources_table = create_resources_table()

# get the clients requests.
while True:
    client_socket, client_address = server.accept()
    print 'Connection from: ', client_address
    massage = client_socket.recv(1024)
    while not massage == '':
        # print 'Received: '
        # print massage,
        to_send = get_response(massage)
        client_socket.send(to_send)
        # print 'Sent: '
        # print to_send,
        massage = client_socket.recv(1024)

    print 'Client disconnected'
    client_socket.close()
