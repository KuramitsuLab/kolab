os.kill(os.getpid(), signal.SIGUSR1)
bytes.fromhex('4a4b4c').decode('utf-8')
all(x == myList[0] for x in myList)
print('%*s : %*s' % (20, 'Python', 20, 'Very Good'))
res = {k: v for k, v in list(kwargs.items()) if v is not None}
res = dict((k, v) for k, v in kwargs.items() if v is not None)
subprocess.check_output('ps -ef | grep something | wc -l', shell=True)
join(['a', 'b', 'c'])
pd.Series(list(set(s1).intersection(set(s2))))
client.send('HTTP/1.0 200 OK\r\n')
then = datetime.datetime.strptime(when, '%Y-%m-%d').date()
inputString.split('\n')
split('\n')
join(str(x) for x in b)
Entry.objects.filter()[:1].get()
a.sum(axis=1)
warnings.simplefilter('always')
print(' '.join(map(str, l)))
subprocess.call(['python.exe', 'hello.py', 'htmlfilename.htm'])
my_float = float(my_string.replace(',', ''))
float('123,456.908'.replace(',', ''))
sys.path.append('/path/to/whatever')
re.split('(\\W+)', 'Words, words, words.')
file = open('Output.txt', 'a')
urllib.request.urlretrieve('http://www.example.com/songs/mp3.mp3', 'mp3.mp3')
r = requests.get(url)
parser.add_argument('--version', action='version', version='%(prog)s 2.0')
i: d[i] 
i in d
i != 'c'
pd.merge(split_df, csv_df, on=['key'], suffixes=('_left', '_right'))
s.split(' ', 4)
input('Enter your input:')
app.run(debug=True)
pickle.dump(mylist, open('save.txt', 'wb'))
scipy.tensordot(P, T, axes=[1, 1]).swapaxes(0, 1)
numpy.zeros((3, 3, 3))
join(content.split(' ')[:-1])
x = np.asarray(x).reshape(1, -1)[(0), :]
sum(sum(i) if isinstance(i, list) else i for i in L)
struct.unpack('!f', '470FC614'.decode('hex'))[0]
my_dict.update((x, y * 2) for x, y in list(my_dict.items()))
subprocess.call('sleep.sh', shell=True)
join(l)
myList = ','.join(map(str, myList))
list(reversed(list(range(10))))
print('lamp, bag, mirror'.replace('bag,', ''))
join(s.split('.')[::-1])
datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')
time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(1236472051807 / 1000.0))
datetime.datetime.now() - datetime.timedelta(days=7)
date()
print(sum(row[column] for row in data))
sum(row[i] for row in array) for i in range(len(array[0]))
base64.b64encode(bytes('your string', 'utf-8'))
dict((k, [d[k] for d in dicts]) for k in dicts[0])
d[k] for d in dicts
k in dicts[0]
k for k, v in list(Counter(mylist).items()) if v > 1
sys.path.insert(1, os.path.join(os.path.dirname(__file__), 'apps'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'subdir'))
db.execute
10
None
image for menuitem in list_of_menuitems for image in menuitem
a.extend(b)
np.savetxt('c:\\data\\np.txt', df.values, fmt='%d')
df.to_csv('c:\\data\\pandas.txt', header=None, index=None, sep=' ', mode='a')
print(x.rpartition('-')[0])
print(x.rsplit('-', 1)[0])
ftp.storlines('STOR ' + filename, open(filename, 'r'))
browser.execute_script
document.getElementById('XYZ').value
1
np.maximum([2, 3, 4], [1, 5, 2])
print(l[3:] + l[:3])
int(1000 * random.random()) for i in range(10000)
db.GqlQuery('SELECT * FROM Schedule WHERE station = $1', foo.key())
df.b.str.contains('^f')
print('\n'.join('\t'.join(str(col) for col in row) for row in tab))
df.set_index(list('BC')).drop(tuples, errors='ignore').reset_index()
format(self.goals, self.penalties)
format(self.goals, self.penalties)
0.
0.
format(self)
int(''.join(str(d) for d in x)) for x in L
join(str(d) for d in x) for x in L
L = [int(''.join([str(y) for y in x])) for x in L]
myfile.write('\n'.join(lines))
x for x in ['AAT', 'XAC', 'ANT', 'TTA'] if 'X' not in x and 'N' not in x
text = re.sub('\\b(\\w+)( \\1\\b)+', '\\1', text)
df.astype(bool).sum(axis=1)
re.search('(?<!Distillr)\\\\AcroTray\\.exe', 'C:\\SomeDir\\AcroTray.exe')
split()
print(re.search('>.*<', line).group(0))
open(filename, 'w').close()
datetime.datetime.strptime(string_date, '%Y-%m-%d %H:%M:%S.%f')
index for index, item in enumerate(thelist) if item[0] == '332'
re.sub('[^\\sa-zA-Z0-9]', '', text).lower().strip()
re.sub('(?!\\s)[\\W_]', '', text).lower().strip()
plt.plot(x, y, label='H\u2082O')
plt.plot(x, y, label='$H_2O$')
x for x in mylist if len(x) == 3
lst = [Object() for _ in range(100)]
lst = [Object() for i in range(100)]
self.driver.find_element_by_css_selector('.someclass a').get_attribute('href')
df1.merge(df2, on='Date_Time')
geo.tif
distutils.dir_util.mkpath(path)
re.sub('\\bH3\\b', 'H1', text)
re.sub('\\D', '', 'aas30dsa20')
join([x for x in 'aas30dsa20' if x.isdigit()])
print(soup.find('name').string)
records = dict((record['_id'], record) for record in cursor)
np.concatenate((A, B))
np.vstack((A, B))
os.stat(filepath).st_size
l.count('a')
Counter(l)
l.count(x)
x in set(l)
dict(((x, l.count(x)) for x in set(l)))
l.count('b')
shutil.copy(srcfile, dstdir)
max(k for k, v in x.items() if v != 0)
k for k, v in x.items() if v != 0
max(k for k, v in x.items() if v != 0)
file.seek(0)
df['c'] = np.where(df['a'].isnull, df['b'], df['a'])
del d['ele'
MyModel.objects.update(timestamp=F('timestamp') + timedelta(days=36524.25))
+ ['was'] + ['annoying']
str(int(x) + 1).zfill(len(x))
all(df.index[:-1] <= df.index[1:])
list(t)
tuple(l)
level1 = map(list, level1)
pprint.pprint(dataobject, logFile)
df.loc[df['BoolCol']]
df.iloc[np.flatnonzero(df['BoolCol'])]
df[df['BoolCol'] == True].index.tolist()
df[df['BoolCol']].index.tolist()
os.chdir(owd)
c.execute
decode('string_escape')
raw_string.decode('string_escape')
raw_byte_string.decode('unicode_escape')
m.group(0) for m in re.finditer('(\\d)\\1*', s)
plt.scatter(np.random.randn(100), np.random.randn(100), facecolors='none')
plt.plot(np.random.randn(100), np.random.randn(100), 'o', mfc='none')
soup.find('div', id='main-content').decompose()
df[df['ids'].str.contains('ball')]
df.reset_index(level=0, inplace=True)
df['index1'] = df.index
df.reset_index(level=['tick', 'obs'])
x[::-1] for x in b
np.array([zip(x, y) for x, y in zip(a, b)])
np.array(zip(a.ravel(), b.ravel()), dtype='i4,i4').reshape(a.shape)
join([str(i) for i in list_of_ints])
requests.post(url, data=DATA, headers=HEADERS_DICT, auth=(username, password))
rfind('}')
print([item for item in [1, 2, 3]])
x['x']
x['y']
x in d
print(os.path.splitext(os.path.basename('hemanth.txt'))[0])
dict(x[i:i + 2] for i in range(0, len(x), 2))
values = sum([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']], [])
df = df[(df['closing_price'] >= 99) & (df['closing_price'] <= 101)]
df.replace({'\n': '<br>'}, regex=True)
df.replace({'\n': '<br>'}, regex=True)
x + y
y in zip(word, word[1:])
list(map(lambda x, y: x + y, word[:-1], word[1:]))
print(re.findall('(https?://[^\\s]+)', myString))
print(re.search('(?P<url>https?://[^\\s]+)', myString).group('url'))
re.sub('[^A-Za-z0-9]+', '', mystring)
pd.date_range('2016-01-01', freq='WOM-2FRI', periods=13)
matrix = [[a, b], [c, d], [e, f]]
mystring.replace(' ', '_')
os.path.abspath('mydir/myfile.txt')
join(my_string.split())
os.path.splitext(filename)[0]
sum(l[:i]) for i, _ in enumerate(l)
Docs/src/Scripts/temp
replace('/', '/\x00/').split('\x00')
np.random.shuffle(np.transpose(r))
df['D'] = df['B']
list(data['A']['B'].values())[0]['maindata'][0]['Info']
all(predicate(x) for x in string)
os.statvfs('/').f_files - os.statvfs('/').f_ffree
user_list = [int(number) for number in user_input.split(',')]
int(s) for s in user.split(',')
ut.sort(key=cmpfun, reverse=True)
ut.sort
key=lambda x: x.count
reverse=True
ut.sort
key=lambda x: x.count
reverse=True
driver.find_element_by_partial_link_text('Send').click()
driver.findElement(By.linkText('Send InMail')).click()
driver.find_element_by_link_text('Send InMail').click()
+ str(i)
open('outfile', 'w').write('#test firstline\n' + open('infile').read())
l.sort
key=lambda t: len(t[1])
reverse=True
re.findall('\\b(\\w+)d\\b', s)
bool(re.search('ba[rzd]', 'foobarrrr'))
list(set(t))
list(set(source_list))
list(OrderedDict.fromkeys('abracadabra'))
numpy.array(a).reshape(-1).tolist()
numpy.array(a)[0].tolist()
print(soup.find(text='Address:').findNext('td').contents[0])
join([('%d@%d' % t) for t in l])
join([('%d@%d' % (t[0], t[1])) for t in l])
driver.execute_script('return document.documentElement.outerHTML;')
i for i in teststr if re.search('\\d+[xX]', i)
df['A'][(df['B'] > 50) & (df['C'] == 900)]
sorted(o.items())
sorted(d)
int('1')
int()
T2 = [map(int, x) for x in T1]
subprocess.call(['./test.sh'])
subprocess.call(['notepad'])
val for pair in zip(l1, l2) for val in pair
encoded = base64.b64encode('data to be encoded')
encoded = 'data to be encoded'.encode('ascii')
lol = list(csv.reader(open('text.txt', 'rb'), delimiter='\t'))
getattr(my_object, my_str)
print(dict(zip(LD[0], zip(*[list(d.values()) for d in LD]))))
d = ast.literal_eval
1
1
word for word in mystring.split() if word.startswith('$')
text = re.sub('^https?:\\/\\/.*[\\r\\n]*', '', text, flags=re.MULTILINE)
np.where(np.in1d(A, [1, 3, 4]).reshape(A.shape), A, 0)
np.mean(a, axis=1)
subprocess.call(['/usr/bin/Rscript', '--vanilla', '/pathto/MyrScript.r'])
subprocess.call('/usr/bin/Rscript --vanilla /pathto/MyrScript.r', shell=True)
writer.writeheader()
df.fillna(df.mean(axis=1), axis=1)
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))
super(Derived, cls).do(a)
a[np.where((a[:, (0)] == 0) * (a[:, (1)] == 1))]
re.split(' +', 'hello world sample text')
len(max(words, key=len))
result[0]['from_user']
line.split() for line in open('File.txt')
res = dict((v, k) for k, v in a.items())
new_file = open('path/to/FILE_NAME.ext', 'w')
any(key.startswith('EMP$$') for key in dict1)
value for key, value in list(dict1.items()) if key.startswith('EMP$$')
pd.DataFrame({'email': sf.index, 'list': sf.values})
print('\t'.join(map(str, list)))
print('\xd0\xbf\xd1\x80\xd0\xb8'.encode('raw_unicode_escape'))
encode('latin-1').decode('utf-8')
image = image.resize((x, y), Image.ANTIALIAS)
re.findall('n(?<=[^n]n)n+(?=[^n])(?i)', s)
print('{0:.0f}%'.format(1.0 / 3 * 100))
mylist.sort
key=lambda x: x['title']
l.sort
key=lambda x: x['title']
l.sort
key=lambda x: (x['title'], x['title_url'], x['id'])
heapq.nlargest
10
range(len(l1))
key=lambda i: abs(l1[i] - l2[i])
soup.find_all('span', {'class': 'starGryB sp'})
df.to_sql('test', engine, schema='a_schema')
brackets = re.sub('[^(){}[\\]]', '', s)
list(dict((x[0], x) for x in L).values())
line.rstrip('\n') for line in file
i for (i, x) in enumerate(testlist) if (x == 1)
i for (i, x) in enumerate(testlist) if (x == 1)
print(testlist.index(element))
lis, key=lambda item: item[1]
0
max(lis, key=itemgetter(1))[0]
time.sleep(1)
join('(' + ', '.join(i) + ')' for i in L)
b = models.CharField(max_length=7, default='0000000', editable=False)
sorted(list5, lambda x: (degree(x), x))
n for n in [1, 2, 3, 5]
newlist = [v for i, v in enumerate(oldlist) if i not in removelist]
f = open('yourfile.txt', 'w')
getattr(obj, 'attr')
map(lambda a: a[0], (('aa',), ('bb',), ('cc',)))
zip(*[('a', 1), ('b', 2), ('c', 3), ('d', 4)])
zip(*[('a', 1), ('b', 2), ('c', 3), ('d', 4)])
result = ([a for (a, b) in original], [b for (a, b) in original])
result = ((a for (a, b) in original), (b for (a, b) in original))
zip(*[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e',)])
map(None, *[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e',)])
json.dumps(Decimal('3.9'))
d['mynewkey'] = 'mynewvalue'
data.update({'a': 1, })
data.update(dict(a=1))
data.update(a=1)
max([max(i) for i in matrix])
answer = str(round(answer, 2))
ip = re.findall('[0-9]+(?:\\.[0-9]+){3}', s)
df.groupby('A').filter(lambda x: len(x) > 1)
x for x in myfile.splitlines() if x != ''
lst = map(int, open('filename.txt').readlines())
plt.colorbar(mappable=mappable, cax=ax3)
Counter(' '.join(df['text']).split()).most_common(100)
list(itertools.combinations((1, 2, 3), 2))
datetime.now(pytz.utc)
list2 = [x for x in list1 if x != []]
list2 = [x for x in list1 if x]
return HttpResponse(data, mimetype='application/json')
re.findall('(.*?)\\[.*?\\]', example_str)
re.findall('(.*?)(?:\\[.*?\\]|$)', example_str)
re.findall('\\(.+?\\)|\\w', '(zyx)bc')
re.findall('\\((.*?)\\)|(\\w)', '(zyx)bc')
re.findall('\\(.*?\\)|\\w', '(zyx)bc')
elements = ['%{0}%'.format(element) for element in elements]
subprocess.Popen(['background-process', 'arguments'])
mydict[x] for x in mykeys
dict([('Name', 'Joe'), ('Age', 22)])
data.reshape(-1, j).mean(axis=1).reshape(data.shape[0], -1)
print(s.encode('unicode-escape').replace('""', '\\""'))
re.split('(\\W+)', s)
i[1]
i[0] for i in list(myDictionary.items())
i for i, j in enumerate(myList) if 'how' in j.lower() or 'what' in j.lower()
isinstance(obj, str)
isinstance(o, str)
type(o) is str
isinstance(o, str)
isinstance(obj_to_test, str)
list2.extend(list1)
list1.extend(mylog)
c.extend(a)
b.append((a[0][0], a[0][2]))
app.config['SECRET_KEY'] = 'Your_secret_string'
pd.DataFrame(out.tolist(), columns=['out-1', 'out-2'], index=out.index)
x for x in range(len(stocks_list)) if stocks_list[x] == 'MSFT'
ax.set_xticklabels(labels, rotation=45)
re.sub('[^\\w]', ' ', s)
os.path.basename(os.path.dirname(os.path.realpath(__file__)))
re.findall
0-7
1
3
re.split('[ ](?=[A-Z]+\\b)', input)
re.split('[ ](?=[A-Z])', input)
r = requests.post(url, files=files, headers=headers, data=data)
open('filename', 'wb').write(bytes_)
dct[k] for k in lst
x.set_index('name').index.get_duplicates()
round(1.923328437452, 3)
li, key=lambda x: datetime.strptime(x[1], '%d/%m/%Y'), reverse=True
ax.set_rlabel_position(135)
os.path.isabs(my_path)
len(list(yourdict.keys()))
len(set(open(yourdictfile).read().split()))
df.groupby('id').first()
pd.concat([df[0].apply(pd.Series), df[1]], axis=1)
re.findall('src=""js/([^""]*\\bjquery\\b[^""]*)""', data)
sum(int(float(item)) for item in [_f for _f in ['', '3.4', '', '', '1.0'] if _f])
subprocess.Popen(['c:\\Program Files\\VMware\\VMware Server\\vmware-cmd.bat'])
q.put((-n, n))
df['group'].plot(kind='bar', color=['r', 'g', 'b', 'r', 'g', 'b', 'r'])
re.findall('([a-fA-F\\d]{32})', data)
len(my_list)
len(l)
len(s)
len(my_tuple)
len(my_string)
decode('string_escape')
replace('a', '%temp%').replace('b', 'a').replace('%temp%', 'b')
shutil.rmtree('/folder_name')
data['weekday'] = data['my_dt'].apply(lambda x: x.weekday())
sorted(x, key=x.get, reverse=True)
list(x.items())
key=lambda pair: pair[1]
reverse=True
np.vstack((a, b))
print(concatenate((a, b), axis=0))
print(concatenate((a, b), axis=1))
c = np.r_[(a[None, :], b[None, :])]
np.array((a, b))
print(socket.getaddrinfo('google.com', 80))
df.xs('sat', level='day', drop_level=False)
return HttpResponse('Unauthorized', status=401)
Flask(__name__, template_folder='wherever')
session.execute('INSERT INTO t1 (SELECT * FROM t2)')
c2.sort
key=lambda row: row[2]
matplotlib.rc('font', **{'sans-serif': 'Arial', 'family': 'sans-serif'})
df['date'].apply(lambda x: x.toordinal())
element.get_attribute('innerHTML')
df.index.get_loc('bob')
os.system('gnome-terminal -e \'bash -c ""sudo apt-get update; exec bash""\'')
my_dict.update({'third_key': 1})
my_list = []
my_list.append(12)
myList.insert(0, 'wuggah')
replace('\\x', '').decode('hex')
df[df.columns[-1]]
df.loc[df['Letters'] == 'C', 'Letters'].values[0]
np.column_stack(([1, 2, 3], [4, 5, 6]))
type(i)
type(v)
type(v)
type(v)
type(v)
print(type(variable_name))
next(itertools.islice(range(10), 5, 5 + 1))
print('""{}""'.format(word))
join(list)
y = [[] for n in range(2)]
data = [line.strip() for line in open('C:/name/MyDocuments/numbers', 'r')]
join([char for char in 'it is icy' if char != 'i'])
re.sub('i', '', 'it is icy')
it is icy
replace('i', '')
df.dropna(subset=[1])
x for x in myList if x.n == 30
nums = [int(x) for x in intstringlist]
map(int, eval(input('Enter the unfriendly numbers: ')))
sys.stdout.write('.')
int(round(2.51 * 100))
df.plot(legend=False)
generator = iter_iprange('192.168.1.1', '192.168.255.255', step=1)
sum(1 << i for i, b in enumerate(x) if b)
target.write('%r\n%r\n%r\n' % (line1, line2, line3))
y for x in data for y in (x if isinstance(x, list) else [x])
print('foo\nbar'.encode('string_escape'))
join(s.rsplit(',', 1))
x[1:] + x[:-1]
2
x[:-1] + (x[1:] - x[:-1]) / 2
arr = numpy.fromiter(codecs.open('new.txt', encoding='utf-8'), dtype='<U2')
l = sorted(l, key=itemgetter('time'), reverse=True)
l = sorted
l, key=lambda a: a['time'], reverse=True
df.loc[df[0].str.contains('(Hel|Just)')]
re.search('\\[(.*)\\]', your_string).group(1)
fox is brown
count('brown')
json.loads(request.body)
urllib.request.urlretrieve(url, file_name)
text.split()
text.split(',')
line.split()
re.sub('(?<!\\d)\\.(?!\\d)', ' ', i) for i in s
list_of_strings, key=lambda s: s.split(',')[1]
subprocess.check_call('vasp | tee tee_output', shell=True)
element for element in lst if isinstance(element, int)
element for element in lst if not isinstance(element, str)
newlist = sorted
list_to_be_sorted, key=lambda k: k['name']
newlist = sorted(l, key=itemgetter('name'), reverse=True)
join(trans['category'])
join(['A', 'B', 'C', 'D'])
json.load(urllib.request.urlopen('url'))
x for x in sents if not x.startswith('@$\t') and not x.startswith('#')
Entry.objects.filter(pub_date__contains='08:00')
list.sort
key=lambda item: (item['points'], item['time'])
t - datetime.datetime(1970, 1, 1)
total_seconds()
re.sub('(\\_a)?\\.([^\\.]*)$', '_suff.\\2', 'long.file.name.jpg')
struct.unpack('H', struct.pack('h', number))
numlist = [float(x) for x in numlist]
df.to_csv(filename, index=False)
json_data = json.loads(unescaped)
chr(i) for i in range(127)
newFile.write(struct.pack('5B', *newFileBytes))
re.sub('^[A-Z0-9]*(?![a-z])', '', string)
list(dict.keys())[-1]
print('hi there', file=f)
s.encode('iso-8859-15')
AuthorizedEmail.objects.filter(group=group).order_by('-added')[0]
re.findall('Test([0-9.]*[0-9]+)', text)
re.findall('Test([\\d.]*\\d+)', text)
os.system('powershell.exe', 'script.ps1')
b.sort
key=lambda x: x[1][2]
list(cf.get_range().get_keys())
datetime.datetime.now()
next(i for i, x in enumerate(lst) if not isinstance(x, bool) and x == 1)
a[:] = [(x - 13) for x in a]
random.choice(os.listdir('C:\\'))
max(x.min(), x.max(), key=abs)
re.findall('""(http.*?)""', s, re.MULTILINE | re.DOTALL)
re.findall('http://[^t][^s""]+\\.html', document)
mystring.replace(' ', '! !').split('!')
open(path, 'r')
sum(item) for item in zip(*items)
items in zip(*data)
a[:, (np.newaxis)]
sum(d * 10 ** i for i, d in enumerate(x[::-1]))
r = int(''.join(map(str, x)))
datetime.strptime('2010-11-13 10:33:54.227806', '%Y-%m-%d %H:%M:%S.%f')
sum(j) / len(j)
j in list(d.items())
zip([1, 2], [3, 4])
0
format(i) for i in a
re.sub('(?<!\\S)((\\S+)(?:\\s+\\2))(?:\\s+\\2)+(?!\\S)', '\\1', s)
df.div(df.sum(axis=1), axis=0)
map(lambda t: (t[1], t[0]), mylist)
t[1]
t[0]
t in mylist
re.findall('\\[[^\\]]*\\]|\\([^\\)]*\\)|""[^""]*""|\\S+', strs)
print(list(itertools.combinations({1, 2, 3, 4}, 3)))
df[['hour', 'weekday', 'weeknum']] = df.apply(lambdafunc, axis=1)
soup.find_all('a', string='Elsie')
my_datetime.strftime('%B %d, %Y')
int(''.join(c for c in s if c.isdigit()))
dic['Test'].update({'class': {'section': 5}})
dict(map(int, x.split(':')) for x in s.split(','))
np.where((vals == (0, 1)).all(axis=1))
dict([['two', 2], ['one', 1]])
dict(zip(l[::2], l[1::2]))
GRAVITY = 9.8
re.findall('(([0-9]+)([A-Z]))', '20M10000N80M')
re.findall('([0-9]+|[A-Z])', '20M10000N80M')
re.findall('([0-9]+)([A-Z])', '20M10000N80M')
re.compile('\\w+').findall('Hello world, my name is...James the 2nd!')
datetime.datetime.strptime('03:55', '%H:%M').time()
requests.get('https://www.reporo.com/', verify=False)
a[a != 0]
new_dict = {k: v for k, v in zip(keys, values)}
dict((k, v) for k, v in zip(keys, values))
dict([(k, v) for k, v in zip(keys, values)])
m = re.search('\\[(\\w+)\\]', s)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
list3 = [(a + b) for a, b in zip(list1, list2)]
ord(c) for c in s.decode('hex')
student_tuples, key=lambda t: (-t[2], t[0])
y for x in range(3) for y in [x, x]
txt = open('file.txt').read()
myList[:] = [(x / myInt) for x in myList]
df.replace(' ', '_', regex=True)
datetime.datetime.combine(my_date, datetime.time.min)
tst2 = str(tst)
time.ctime(os.path.getmtime(file))
time.ctime(os.path.getctime(file))
t = os.path.getmtime(filename)
os.path.getmtime(path)
print(('last modified: %s' % time.ctime(os.path.getmtime(file))))
print(('created: %s' % time.ctime(os.path.getctime(file))))
return os.path.getctime(path_to_file)
os.system('TASKKILL /F /IM firefox.exe')
return 
x.group(0) for x in re.finditer
A-Za-z
+""
join(['%.2f'] * len(x))
print(re.match('(\\d+(\\.\\d+)?)', '3434.35353').group(1))
df['name'].str.replace('\\(.*\\)', '')
result = [x for x in list_a if x[0] in list_b]
print([''.join(a) for a in combinations(['hel', 'lo', 'bye'], 2)])
x for x in li if 'ar' in x[2]
unsorted_list.sort
key=lambda x: x[3]
logging.info('test')
fig.add_subplot(1, 1, 1)
sorted(list(x.items()), key=operator.itemgetter(1))
sorted(dict1, key=dict1.get)
sorted(d, key=d.get, reverse=True)
sorted(list(d.items()), key=(lambda x: x[1]))
np.einsum('ijk,ikl->ijl', A, B)
print('I have: {0.price}'.format(card))
f.write('# Data for Class A\n')
a = a[-1:] + a[:-1]
datetimevariable.strftime('%Y-%m-%d')
mixed.replace('\r\n', '\n').replace('\r', '\n')
os.path.expanduser('~user')
T = [L[i] for i in Idx]
words = open('myfile').read().split()
sum([x[1] for x in i])
i in data
sum([x[1] for x in i]) for i in data
Article.objects.annotate(like_count=Count('likes')).order_by('-like_count')
today = datetime.datetime.utcnow().date()
a * b
b in zip(lista, listb)
re.findall('(?::|;|=)(?:-)?(?:\\)|\\(|D|P)', s)
re.match('[:;][)(](?![)(])', str)
json_string = json.dumps([ob.__dict__ for ob in list_name])
listofzeros = [0] * n
stringnamehere.decode('utf-8', 'ignore')
re.findall('((?:A|B|C)D)', 'BDE')
dic.setdefault(key, []).append(value)
a[np.argmin(a[:, (1)])]
a.update(b)
k: v
v in d.items() 
k != 'mykey1'
d in mylist
numpy.random.random((3, 3))
df['C'] = df['A'] + df['B']
value for key, value in list(programs.items()) if 'new york' in key.lower()
sys.path.append('/path/to/main_folder')
re.findall('\\d+(?=[^[]+$)', s)
pickle.load(open('afile', 'rb'))
ex.groupby(level='A').agg(lambda x: x.index.get_level_values(1).nunique())
pd.concat(map(pd.DataFrame, iter(d.values())), keys=list(d.keys())).stack().unstack(0)
sum(1 for i, j in zip(a, b) if i != j)
d = {(a.lower(), b): v for (a, b), v in list(d.items())}
list_.sort
key=lambda x: [x[0], len(x[1]), x[1]]
s.strip()
s = s.lstrip()
s = s.rstrip()
s = s.strip(' \t\n\r')
print(re.sub('[\\s+]', '', s))
Task.objects.exclude(prerequisites__status__in=['A', 'P', 'F'])
root.configure(background='black')
numpy.array([(key, val) for key, val in result.items()], dtype)
pd.concat([df_1, df_2.sort_values('y')])
re.sub('(.*)</div>', '\\1</bad>', s)
d, key=lambda x: (d[x]['salary'], d[x]['bonus'])
Book.objects.filter(author__id=1).filter(author__id=2)
re.compile('XYZ', re.IGNORECASE).split('fooxyzbar')
sum(map(int, s)) for s in example.split()
i for i in y if y[i] == 1
c.decode('unicode_escape')
pd.melt(x, id_vars=['farm', 'fruit'], var_name='year', value_name='value')
default_data['item3'] = 3
default_data.update({'item3': 3, })
default_data.update({'item4': 4, 'item5': 5, })
l[:3] + l[-3:]
df = df.reset_index(drop=True)
a[x].append(b[x]) for x in range(3)
os.path.realpath(path)
set(L[0].f.items()).issubset(set(a3.f.items()))
zip(*np.where(a == 1))
df.columns = df.columns.get_level_values(0)
x = scipy.matrix([1, 2, 3]).transpose()
text = re.sub('(\\bget\\b)', '\\1@', text)
np.array([np.arange(3), np.arange(2, -1, -1), np.ones((3,))]).min(axis=0)
df['new_col'] = list(range(1, len(df) + 1))
os.environ['DEBUSSY'] = '1'
print(os.environ['DEBUSSY'])
os.environ['DEBUSSY'] = '1'
b.update(d)
df['b']
ebar = plt.errorbar(x, y, yerr=err, ecolor='y')
results += [each for each in os.listdir(folder) if each.endswith('.c')]
print('\xc2\xa3'.decode('utf8') + '1')
re.sub('(?<=[a-z])([A-Z])', '-\\1', s).lower()
0
3
format(num)
numpy.append(a, a[0])
df.ix[:, (df.loc[0] == 38.15)].columns
df2['revenue'] = df2.CET.map(df1.set_index('date')['revenue'])
json_data = json.loads(json_string)
math.cos(math.radians(1))
sum(isinstance(x, int) for x in a)
replace('\u200b', '*')
threading.Thread(target=SudsMove).start()
sum(i * i for i in l)
sum(map(lambda x: x * x, l))
d = dict(((key, value) for (key, value) in iterable))
d = {key: value for (key, value) in iterable}
d = {k: v for (k, v) in iterable}
df.round({'Alabama_exp': 2, 'Credit_exp': 3})
p.setopt(pycurl.WRITEFUNCTION, lambda x: None)
print(random.choice(words))
d, key=lambda x: d[x]['count']
int(x) if x else 0
x in data.split(',')
join(x or '0' for x in s.split(','))
re.compile('$^')
re.compile('.\\A|.\\A*|.\\A+')
re.compile('a^')
df.columns[df.max() > 0]
yourdatetime.date() == datetime.today().date()
print('\x1b[1m' + 'Hello')
re.sub('.{20}(.mkv)', '\\1', 'unique12345678901234567890.mkv')
join(mystring.split())
print('{:.100f}'.format(2.345e-67))
Blog.objects.filter(pk__in=[1, 4, 7])
f = open('test/test.pdf', 'rb')
format(12345678.46, ',').replace(',', ' ').replace('.', ',')
pd.merge(frame_1, frame_2, left_on='county_ID', right_on='countyid')
np.isnan(a).sum() / np.prod(a.shape)
iter(cityPopulation.items())
key=lambda k_v: k_v[1][2]
reverse=True
list(u.items())
key=lambda v: v[1]
list(d.items())
key=lambda k_v: k_v[1]
reverse=True
list(d.items())
key=lambda k_v: k_v[1]
f = open(os.path.join(__location__, 'bundled-resource.jpg'))
f = open('words.txt', 'rU')
float(d2[k]) / d1[k]
k in d2
d2[k] / d1[k]
k in list(d1.keys()) & d2
dict((k, float(d2[k]) / d1[k]) for k in d2)
df.to_csv(filename, date_format='%Y%m%d')
my_dict.pop('key', None)
b = np.where(np.isnan(a), 0, a)
subprocess.call('start command -flags arguments', shell=True)
subprocess.call('command -flags arguments &', shell=True)
f = urllib.request.urlopen(url, urllib.parse.unquote(urllib.parse.urlencode(params)))
rstrip()
urllib.parse.quote(s.encode('utf-8'))
np.array(map(int, '100110'))
print(np.array(list(mystr), dtype=int))
img = cv2.imread('messi5.jpg', 0)
lst.sort
key=lambda x: x[2]
reverse=True
subprocess.call('grep -r PASSED *.log | sort -u | wc -l', shell=True)
len(my_text) - len(my_text.rstrip('?'))
df[df.columns[1:]].replace('[\\$,]', '', regex=True).astype(float)
df1.merge(df2, how='left', on='word')
print(''.join(''.join(i) for i in zip(a2, a1)) + a[-1] if len(a) % 2 else '')
root.attributes('-topmost', True)
root.lift()
hex(int(''.join([str(int(b)) for b in walls]), 2))
hex(sum(b << i for i, b in enumerate(reversed(walls))))
print(('Total score for', name, 'is', score))
print('Total score for {} is {}'.format(name, score))
print('Total score for %s is %s  ' % (name, score))
print(('Total score for', name, 'is', score))
url('^$', TemplateView.as_view(template_name='your_template.html'))
df[df['A'].isin([3, 6])]
system('/path/to/my/venv/bin/python myscript.py')
Employees.objects.values_list('eng_name', flat=True)
re.findall('\\d|\\d,\\d\\)', '6,7)')
input('Press Enter to continue...')
encode('hex')
db.Doc.update({'_id': b['_id']}, {'$set': {'geolocCountry': myGeolocCountry}})
re.sub('l+', 'l', 'lollll')
rows = soup.findAll('tr')[4::5]
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
pd.concat([GOOG, AAPL], keys=['GOOG', 'AAPL'], axis=1)
return HttpResponse(json.dumps(response_data), content_type='application/json')
myString.decode('string_escape')
hashlib.md5(open('filename.exe', 'rb').read()).hexdigest()
k for k, v in d.items() if v == desired_value
k for d in LoD for k in list(d.keys())
set([i for s in [list(d.keys()) for d in LoD] for i in s])
i for s in [list(d.keys()) for d in LoD] for i in s
keys, values = zip(*list(d.items()))
int(Decimal(s))
numpy.in1d(b, a).all()
numpy.array([(x in a) for x in b])
networkx.draw_networkx_labels(G, pos, labels)
y = [row[:] for row in x]
X = numpy.loadtxt('somefile.csv', delimiter=',')
matching = [s for s in some_list if 'abc' in s]
df.to_csv('mydf.tsv', sep='\t')
s.rsplit(',', 1)
all(isinstance(x, int) for x in lst)
all(isinstance(x, int) for x in lst)
line.strip()
driver.execute_script('window.scrollTo(0, Y)')
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
datetime.datetime.combine(dateobject, datetime.time())
print(any(x in a for x in b))
scipy.misc.imsave('outfile.jpg', image_array)
item = re.sub(' ?\\([^)]+\\)', '', item)
item = re.sub(' ?\\(\\w+\\)', '', item)
item = re.sub(' \\(\\w+\\)', '', item)
len(set(list1).intersection(list2)) > 0
i = int(s, 16)
int('0xff', 16)
int('FFFF', 16)
ast.literal_eval('0xdeadbeef')
int('deadbeef', 16)
os.system('screencapture screen.png')
driver.set_window_size(1400, 1000)
unicodedata.normalize('NFKD', 'm\xfasica').encode('ascii', 'ignore')
pandas.concat([df1, df2]).drop_duplicates().reset_index(drop=True)
a = numpy.fromfile('filename', dtype=numpy.float32)
subprocess.call('mv /home/somedir/subdir/* somedir/', shell=True)
print('\u25b2'.encode('utf-8'))
difflib.SequenceMatcher(None, file1.read(), file2.read())
dict((k, int(v)) for k, v in (e.split(' - ') for e in s.split(',')))
all(i in (1, 2, 3, 4, 5) for i in (1, 6))
df['Date'].map(lambda t: t.date()).unique()
7
format(mystring)
open('ComponentReport-DJI.xls', 'rb').read(200)
df.sort_values(['b', 'c'], ascending=[True, False], inplace=True)
df.sort_values(['a', 'b'], ascending=[True, False])
df1.sort(['a', 'b'], ascending=[True, False], inplace=True)
df.sort(['a', 'b'], ascending=[True, False])
redirect('Home.views.index')
x for x in a if x not in [2, 3, 7]
out = ''.join(c for c in asking if c not in ('!', '.', ':'))
soup.find('meta', {'name': 'City'})['content']
urllib.parse.unquote('%0a')
urllib.parse.unquote(url).decode('utf8')
del lst[:]
del lst1[:]
lst[:] = []
alist[:] = []
s.reset_index(0).reset_index(drop=True)
elems[0].getText().encode('utf-8')
y - x
y in zip(L, L[1:])
print(re.search('\\bLOG_ADDR\\s+(\\S+)', line).group(1))
globals
update(importlib.import_module('some.package').__dict__)
join(['a', 'b', 'c', 'd'])
url.split('&')
od = collections.OrderedDict(sorted(d.items()))
OrderedDict(sorted(list(d.items()), key=(lambda t: t[0])))
response = requests.put(url, data=json.dumps(data), headers=headers)
re.sub('[\\W_]+', '', s)
x + y
x in l2 for y in l1
dict([x.split('=') for x in s.split()])
my_list.pop(2)
s = s.replace('M', '')
sum(x * y for x, y in zip(a, b))
list(x * y for x, y in list(zip(a, b)))
sum(i * j for i, j in zip(a, b))
sum(x * y for x, y in list(zip(a, b)))
f.write(open('xxx.mp4', 'rb').read())
new_list = [(x + 1) for x in my_list]
x for x in j if x >= 5
plt.plot(list(range(10)), '--bo')
plt.plot(list(range(10)), linestyle='--', marker='o', color='b')
i.split('\t', 1)[0] for i in l
myList = [i.split('\t')[0] for i in myList]
sum(your_list)
ForkedPdb().set_trace()
result = {k: d2.get(v) for k, v in list(d1.items())}
datetime.datetime.now() + datetime.timedelta(days=1, hours=3)
dict((v, k) for k, v in my_dict.items())
L, key=lambda x: int(x.split('.')[2])
any(d['name'] == 'Test' for d in label)
a[:] = [x for x in a if x != [1, 1]]
x for x in a if x != [1, 1]
a[i]
a[i + 1] for i in range(0, len(a), 2)
len(set(a)) == len(a)
print(hashlib.md5(open(full_path, 'rb').read()).hexdigest())
join(x.upper() if random.randint(0, 1) else x for x in s)
os.system('GREPDB=""echo 123""; /bin/bash -c ""$GREPDB""')
os.system('/bin/bash -c ""echo hello world""')
getattr(test, a_string)
Image.open('pathToFile').show()
files.sort(key=file_number)
sentence.replace(' ', '')
sentence.strip()
sentence = re.sub('\\s+', '', sentence, flags=re.UNICODE)
sentence = ''.join(sentence.split())
sum(my_counter.values())
np.sqrt(((A - B) ** 2).sum(-1))
levels = [{}, {}, {}]
weekly = [sum(visitors[x:x + 7]) for x in range(0, len(daily), 7)]
del d[key
i: a[i] 
i in a
if (i != 0)
lol.pop('hello')
del r[key
np.linalg.solve(np.dot(a.T, a), np.dot(a.T, b))
pd.concat([df.drop('b', axis=1), pd.DataFrame(df['b'].tolist())], axis=1)
x['content'].lower()
x in messages
join(my_list)
re.sub('(http://\\S+|\\S*[^\\w\\s]\\S*)', '', a)
str(n) == str(n)[::-1]
ftp.storbinary('STOR myfile.txt', open('myfile.txt', 'rb'))
re.sub('.*I', 'I', stri)
int('1,000,000'.replace(',', ''))
pd.merge(df1, df2, left_index=True, right_index=True, how='outer')
all(dict.values())
df.c_contofficeID.str.replace('^12(?=.{4}$)', '')
L[::(-1)]
reversed(array)
L.reverse()
list(reversed(array))
tup[0] for tup in A
newcontents = contents.replace('a', 'e').replace('s', '3')
json.dumps([dict(list(row.items())) for row in rs])
config_file = os.path.expanduser('~/foo.ini')
request.params.getall('c')
np.corrcoef(x)
print(max(1, 2, 3))
self.request.get('var_name')
a['x'].apply(lambda x, y: x + y, args=(100,))
User.objects.order_by('-pet__age')[:10]
time.sleep(5)
time.sleep(60)
sleep(0.1)
time.sleep(60)
time.sleep(0.1)
x for x in my_list if not any(c.isdigit() for c in x)
df['state'].apply(lambda x: x[len(x) / 2 - 1:len(x) / 2 + 1])
plt.grid(True)
lst, key=lambda x: (-1 * c[x], lst.index(x))
max(len(str(x)) for x in line) for line in zip(*foo)
df.Country.value_counts().reset_index(name='Sum of Accidents')
data.set_index('Date').diff()
a.update([3, 4])
a[1::2] = -1
df.groupby('group')['value'].rank(ascending=False)
datetime.strptime('Tue, 22 Nov 2011 06:00:00 GMT', '%a, %d %b %Y %H:%M:%S %Z')
struct.pack('<I', 1633837924)
list.append('foo')
list.insert(0, 'foo')
theset = set(k.lower() for k in thedict)
format(s='dog', n=5, c='x')
isinstance(s, str)
isinstance(s, str)
dict(pair for d in L for pair in list(d.items()))
k: v
d in L for k, v in list(d.items())
df.sort_values(['Peak', 'Weeks'], ascending=[True, False], inplace=True)
df.sort(['Peak', 'Weeks'], ascending=[True, False], inplace=True)
print('Hello')
1
4
2
4
1
4
1
5
list(itertools.product(*a))
df.groupby(['Country', 'Item_Code'])[['Y1961', 'Y1962', 'Y1963']].sum()
done = [(el, x) for el in [a, b, c, d]]
x = x[numpy.logical_not(numpy.isnan(x))]
os.path.join(*x.split(os.path.sep)[2:])
line = line.replace(';', ':')
subprocess.call('tar c my_dir | md5sum', shell=True)
437
decode('hex')
k for k, v in User._fields.items() if v.required
df = df.ix[:, 0:2]
x = map(int, x.split())
x = [int(i) for i in x.split()]
driver.find_element_by_css_selector
onclick*='1 Bedroom Deluxe'
webbrowser.open('file:///my_pdf.pdf')
result = result.replace('\\', '')
result.replace('\\', '')
df.replace('-', 'NaN')
datetime.datetime.now().date()
elem.tag for elem in a.iter()
elem.tag for elem in a.iter() if elem is not a
lst, key=lambda x: x['language'] != 'en'
all(value == 0 for value in list(your_dict.values()))
df.pivot_table('Y', rows='X', cols='X2')
M.sum(axis=0).sum(axis=0)
time.mktime(dt.timetuple()) + dt.microsecond / 1000000.0
df[(x <= df['columnX']) & (df['columnX'] <= y)]
sorted(L, key=itemgetter(2))
l.sort(key=(lambda x: x[2]))
sorted(l, key=(lambda x: x[2]))
sorted_list = sorted(list_to_sort, key=itemgetter(2, 0, 1))
np.argwhere(np.all(arr == [[0, 3], [3, 0]], axis=(1, 2)))
data.loc[:, (list(itertools.product(['one', 'two'], ['a', 'c'])))]
data.loc[:, ([('one', 'a'), ('one', 'c'), ('two', 'a'), ('two', 'c')])]
hashtags = re.findall('#(\\w+)', str1, re.UNICODE)
os.rename(src, dst)
print(etree.tostring(some_tag.find('strong')))
json.dumps
str(k)
v for k, v in data.items()
soup = BeautifulSoup(response.read().decode('utf-8'))
os.remove(filename)
min([x for x in num_list if x > 2])
df['prod_type'] = 'responsive'
lst, key=lambda x: (x < 0, x)
six_months = (date.today() + relativedelta(months=(+ 6)))
date(2010, 12, 31) + relativedelta(months=(+ 1))
date(2010, 12, 31) + relativedelta(months=(+ 2))
print((datetime.date.today() + datetime.timedelta(((6 * 365) / 12))).isoformat())
list(things.keys())
key=lambda x: things[x]['weight']
reverse=True
a[np.arange(len(a)) != 3]
x for x in lst if fn(x) != 0
df.set_index('month')
arr = [line.split(',') for line in open('./urls-eu.csv')]
i for i in range(100) if i > 10
i < 20
join([c for c in strs if c.isdigit()])
re.split('\\t+', yas.rstrip('\t'))
a.T * b
rstrip()
rstrip('\n')
s.strip()
s.rstrip()
s.lstrip()
rstrip('\r\n')
rstrip('\r\n')
rstrip('\r\n')
rstrip('\n')
re.findall('.{,16}\\b', text)
X[i][j] for j in range(len(X[i]))
i in range(len(X))
encode('latin-1')
df.groupby((df.a == 'B').shift(1).fillna(0).cumsum())
urllib.request.urlretrieve('http://search.twitter.com/search.json?q=hi', 'hi.json')
numpy.where((x == 0))[0]
sys.stdout.flush()
str(i)
a.__str__()
str(a)
L.sort(key=operator.itemgetter(1))
print(str(count) + '    ' + str(conv))
df.fillna(method='ffill', inplace=True)
text.config(state=DISABLED)
sum(map(ord, string))
list(itertools.product(*arrays))
format(value)
df[df.Col1.isin(['men', 'rocks', 'mountains'])]
x[1] for x in L
split()
MyModel.objects.extra(select={'length': 'Length(name)'}).order_by('length')
dicts, key=lambda x: (abs(1.77672955975 - x['ratio']), -x['pixels'])
m.mask
re.findall('\\b[A-Z]', formula)
matrix = [([0] * 5) for i in range(5)]
np.vstack(np.meshgrid(x_p, y_p, z_p)).reshape(3, -1).T
arr[arr != 0].min()
browser.find_elements_by_xpath
type='submit'
browser.find_elements_by_xpath
type='submit'
get_attribute('value')
pd.DataFrame(df.columns[np.argsort(df.values)], df.index, np.unique(df.values))
datetime.datetime.today().strftime('%Y-%m-%d')
urllib.parse.quote_plus('string_of_characters_like_these:$#@=?%^Q^$')
d, key=lambda k: len(d[k]), reverse=True
map(list, zip(*[(1, 2), (3, 4), (5, 6)]))
y in zip(myList, myList[1:]) 
y == 9
driver.get('http://www.google.com.br')
b = a.decode('utf8')[::-1].encode('utf8')
dparser.parse('monkey 2010-07-32 love banana', fuzzy=True)
dparser.parse('monkey 20/01/1980 love banana', fuzzy=True)
dparser.parse('monkey 10/01/1980 love banana', fuzzy=True)
dict(map(lambda s: s.split(':'), ['A:1', 'B:2', 'C:3', 'D:4']))
re.search('[a-zA-Z]', the_string)
DataFrame({'count': df1.groupby(['Name', 'City']).size()}).reset_index()
re.sub('[^0-9]', '', 'sdkjh987978asd098as0980a98sd')
y for y in a if y not in b
df.groupby('ID').head(4)
zip(*l)
dict(zip([1, 2, 3, 4], ['a', 'b', 'c', 'd']))
dict(zip([1, 2, 3, 4], ['a', 'b', 'c', 'd']))
request.url
somestring.replace('\\r', '')
simplejson.dumps(dict([('%d,%d' % k, v) for k, v in list(d.items())]))
datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
parser.parse('Aug 28 1999 12:00AM')
os.path.split(os.path.abspath(existGDBPath))
os.path.dirname(os.path.abspath(existGDBPath))
requests.post('http://httpbin.org/post', json={'test': 'cheers'})
a = [x for x in a if x['link'] not in b]
request.args.get('a')
list(range(11, 17))
data_df['grade'] = data_df['grade'].astype(float).astype(int)
alkaline_earth_values, key=lambda x: x[1]
your_string.strip('0')
list(permutations(list(range(9)), 2))
re.compile('^(.+)(?:\\n|\\r\\n?)((?:(?:\\n|\\r\\n?).+)+)', re.MULTILINE)
re.compile('^(.+)\\n((?:\\n.+)+)', re.MULTILINE)
call(['path/to/python', 'test2.py', 'neededArgumetGoHere'])
a.sort(key=operator.itemgetter(2, 3))
final_choices = ((another_choice,) + my_choices)
final_choices = ((another_choice,) + my_choices)
os.getcwd()
os.path.realpath(__file__)
os.path.dirname(path)
os.path.realpath(path)
dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
full_path = os.path.realpath(__file__)
arr[arr[:, (2)].argsort()]
numpy.sort(arr, axis=0)
re.split('[ .]', 'a b.c')
shutil.copy('file.txt', 'file2.txt')
print(''.join(choice(ascii_uppercase) for i in range(12)))
join(seq) for seq in zip(lst, lst[1:])
data.rename(columns={'gdp': 'log(gdp)'}, inplace=True)
print(soup.get_text())
sorted(li, key=operator.itemgetter(1), reverse=True)
data['sex'].replace([0, 1], ['Female', 'Male'], inplace=True)
re.split('\\W+', 'Words, words, words.')
re.match('(.*?[.?!](?:\\s+.*?[.?!]){0,1})', phrase).group(1)
print([a for a, b in re.findall('((\\w)\\2*)', s)])
print(' '.join(OrderedDict.fromkeys(s)))
print(' '.join(set(s)))
x for x in file.namelist() if x.endswith('/')
input_string.count('Hello')
print('.'.join([item[0] for item in data]))
fh1.seek(2)
print(zip(my_list[0::2], my_list[1::2]))
my_new_list = zip(my_list[0::2], my_list[1::2])
sys.setdefaultencoding('utf8')
datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(re.findall('[\\u0600-\\u06FF]+', my_string))
df.groupby(df.index.map(lambda t: t.minute))
dict['Apple']['American']
df2.dropna(subset=['three', 'four', 'five'], how='all')
a.insert(0, k)
a = a[:n] + k + a[n:]
np.flatnonzero(x).mean()
df['just_date'] = df['dates'].dt.date
x for x in a if x not in b
join(x) for x in a
list(map(''.join, a))
re.split('\n\\s*\n', s)
0
2
format(24322.34)
my_function(**data)
sum((1 for line in open('myfile.txt')))
print(round(1123.456789, -1))
x for y, x in sorted(zip(Y, X))
x for y, x in sorted(zip(Y, X))
datetime.date(2010, 6, 16).isocalendar()[1]
df.iloc
np.r_
1
10
15
17
50
100
df.groupby('dummy').agg({'returns': [np.mean, np.sum]})
s.lower()
s.decode('utf-8').lower()
urlfetch.fetch(url, deadline=10 * 60)
print(my_string[0:100])
legend(numpoints=1)
set(y) & set
d1.get
y in d2.items()
numpy.loadtxt(open('test.csv', 'rb'), delimiter=',', skiprows=1)
Sample.objects.filter(date__range=['2011-01-01', '2011-01-31'])
Sample.objects.filter(date__year='2011', date__month='01')
d['dict3'] = {'spam': 5, 'ham': 6}
numpy.apply_along_axis(numpy.linalg.norm, 1, a)
dict((k, v) for d in dicts for k, v in list(d.items()))
print('your string'.decode('string_escape'))
sum([True, True, False, False, False, True])
fig.set_size_inches(w, h, forward=True)
there %(5)
5
map(int, example_string.split(','))
int(s) for s in example_string.split(',')
x = [i[0] for i in x]
y = map(operator.itemgetter(0), x)
y = [i[0] for i in x]
results = [item['value'] for item in test_data]
datetime.datetime.now().isoformat()
datetime.datetime.utcnow().isoformat()
df.apply(' '.join, axis=0)
pd.DataFrame(df.values - df2.values, columns=df.columns)
print(open('myfile.txt', 'U').read())
print(line.decode('utf-16-le').split())
file = io.open('data.txt', 'r', encoding='utf-16-le')
s1 = pd.merge(df1, df2, how='inner', on=['user_id'])
foo.decode('utf8').encode('utf8')
a.shape
N.shape(a)
N.shape(a)
a.shape
i for i, v in enumerate(L) if v[0] == 53
struct.unpack('<L', 'y\xcc\xa6\xbb')[0]
arr[[0, 1, 1], [1, 0, 2]]
list(powerset('abcd'))
s in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']
urllib.parse.quote('http://spam.com/go/')
plt.savefig('test.svg')
len(myArray)
sys.path.insert(0, './path/to/your/modules/')
cursor.execute('INSERT OR REPLACE INTO master.table1 SELECT * FROM table1')
re.match('[a-zA-Z][\\w-]*\\Z', 'A\n')
re.match('[a-zA-Z][\\w-]*$', '!A_B')
int('deadbeef', 16)
int('a', 16)
int('0xa', 16)
int(s, 16)
int(hexString, 16)
print('Value is ""' + str(value) + '""')
print('Value is ""{}""'.format(value))
tags | join(' ')
help('modules')
x[0]
x in listD[i]
i in range(len(listD))
sorted(s, key=str.upper)
sorted(sorted(s), key=str.upper)
sorted(s, key=str.lower)
pd.merge(df1, df2, on=['A', 'B', 'C', 'D'], how='inner')
dict((v, k) for k, v in map.items())
s.decode('unicode_escape')
int(i) for i in str_list
map(int, ['1', '2', '3'])
list(map(int, ['1', '2', '3']))
soup.find_all('a', href=re.compile('http://www\\.iwashere\\.com/'))
soup.find_all('a', href=re.compile('^(?!(?:[a-zA-Z][a-zA-Z0-9+.-]*:|//))'))
subprocess.call(['java', '-jar', 'Blender.jar'])
cursor.execute('INSERT INTO table (`column1`) VALUES (%s)', (value,))
url = re.sub('\\.com$', '', url)
print(url.replace('.com', ''))
print(', ,'.join([str(i[0]) for i in mytuple]))
max(min(my_value, max_value), min_value)
re.findall('\\w+|[^\\w\\s]', text, re.UNICODE)
result = db.engine.execute('<sql here>')
sys.exit(0)
join(c for c in my_string if c.isdigit())
re.split(' +', str1)
getattr(getattr(myobject, 'id', None), 'number', None)
i * 2
i in range(10)
dict((i, i * 2) for i in range(10))
plt.cla()
total = sum(float(item) for item in s.split(','))
bin(ord('P'))
print(my_string.split(', ', 1)[1])
print(data['places'][0]['post code'])
word = re.sub('([aeiou]):(([aeiou][^aeiou]*){3})$', '\\1\\2', word)
json.loads('{""foo"": 42, ""bar"": ""baz""}')['bar']
data = json.loads(array)
data = json.loads(array)
re.findall('#(\\w+)', 'http://example.org/#comments')
any(e in lestring for e in lelist)
plt.figure(figsize=(3, 4))
s.translate(None, string.punctuation)
base64.urlsafe_b64decode(uenc.encode('ascii'))
len(dict_test) + sum(len(v) for v in dict_test.values())
hex(d).split('x')[1]
list(str(123))
int(x) for x in str(num)
br.select_form(nr=0)
json.load(codecs.open('sample.json', 'r', 'utf-8-sig'))
json.loads(open('sample.json').read().decode('utf-8-sig'))
server = smtplib.SMTP('smtp.gmail.com', 587)
int('{:08b}'.format(n)[::-1], 2)
df.set_index(['d'], append=True)
list(d.items())
list(d.items())
session.query(Task).filter(Task.time_spent > timedelta(hours=3)).all()
os.system('msbuild project.sln /p:Configuration=Debug')
max(list(MyCount.keys()), key=int)
os.system('source .bashrc; shopt -s expand_aliases; nuke -x scriptPath')
my_function.__name__
np.all(a == a[(0), :], axis=0)
a, key=lambda x: (sum(x[1:3]), x[0])
a, key=lambda x: (sum(x[1:3]), x[0]), reverse=True
lst, key=lambda x: (sum(x[1:]), x[0])
lst, key=lambda x: (sum(x[1:]), x[0]), reverse=True
response.headers['WWW-Authenticate'] = 'Basic realm=""test""'
del request.session['mykey'
datetime.datetime.strptime('24052010', '%d%m%Y').date()
re.sub('[^\\x00-\\x7F]+', ' ', text)
myList = [i for i in range(10)]
m[0] for m in re.compile('((.+?)\\2+)').findall('44442(2)2(2)44')
i[0] for i in re.findall('((\\d)(?:[()]*\\2*[()]*)*)', s)
fig.subplots_adjust(wspace=0, hspace=0)
x[::-1]
csvwriter.writerow(row)
item.date | date
re.split('(?<=[\\.\\?!]) ', text)
re.compile('\xe2\x80\x93')
variable = []
intarray = array('i')
sublist[::-1] for sublist in to_reverse[::-1]
join(['I ', '<', '3s U ', '&', ' you luvz me'])
logging.disable(logging.CRITICAL)
cursor.execute('INSERT INTO index(url) VALUES(%s)', (url,))
df['DateStr'] = df['DateObj'].dt.strftime('%d%m%Y')
s.split('@')[0]
df.query('index < @start_remove or index > @end_remove')
df.loc[(df.index < start_remove) | (df.index > end_remove)]
df.isnull().sum()
df.reset_index(inplace=True)
x['value'] for x in list_of_dicts
np.array([[1, 2, 3], [4, 5, 6]]).tolist()
ast.literal_eval('(1,2,3,4)')
dataList.sort
key=lambda x: x[1]
list(map(list, set(map(lambda i: tuple(i), testdata))))
list(i) for i in set(tuple(i) for i in testdata)
return user.groups.filter(name='Member').exists()
return user.groups.filter(name__in=['group1', 'group2']).exists()
logging.getLogger().setLevel(logging.DEBUG)
join(str(i) for i in (34.2424, -64.2344, 76.3534, 45.2344))
join([s[x:x + 2][::-1] for x in range(0, len(s), 2)])
plt.savefig('graph.png', dpi=1000)
my_list = [[x for x in sublist if x not in to_del] for sublist in my_list]
item for item in a if 1 in item
item for item in a if item[0] == 1
p.id
p.id
p in enumerate(p_list)
exec(compile(open('file.py').read(), 'file.py', 'exec'))
rows = session.query(Congress).count()
dfs = pd.read_excel(file_name, sheetname=None)
struct.unpack('d', binascii.unhexlify('4081637ef7d0424a'))
a[tuple(b)]
map(list, permutations([2, 3, 4]))
sorted(unsorted_list, key=presorted_list.index)
d = pd.DataFrame(0, index=np.arange(len(data)), columns=feature_list)
x.find('World')
x.find('Aloha')
index('cc')
index('df')
str.find('a')
str.find('g')
str.find('s', 11)
str.find('s', 15)
str.find('s', 16)
str.find('s', 11, 14)
d, key=lambda x: datetime.datetime.strptime(x, '%m-%Y')
re.split('\\.\\s', text)
4
s.rfind('&')
s[:s.rfind('&')]
driver.find_element_by_xpath
value='"" + state + ""'
click()
open('test', 'a+b').write('koko')
print([i for i in re.split('([\\d.]+|\\W+)', 'x+13.5*10x-4e1') if i])
re.findall('[\u4e00-\u9fff]+', ipath)
s.split('s')
subprocess.Popen(['rm', '-r', 'some.file'])
dict((d['name'], d) for d in listofdict)
datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
time.strftime('%Y-%m-%d %H:%M')
re.findall('[bcdfghjklmnpqrstvwxyz]+', 'CONCERTATION', re.IGNORECASE)
i for i, e in enumerate(a) if e != 0
map(int, re.findall('\\d+', string1))
os.path.dirname(sys.executable)
ax.xaxis.set_label_position('top')
ax.xaxis.tick_top()
ax.xaxis.set_ticks_position('top')
datetime.strptime('2015/01/01 12:12am', '%Y/%m/%d %I:%M%p')
sys.exit(0)
sys.exit('aa! errors!')
sys.exit()
max(abs(x) for x in arr[i:i + 4]) for i in range(0, len(arr), 4)
os.chdir('c:\\Users\\uname\\desktop\\python')
os.chdir(path)
no_integers = [x for x in mylist if not isinstance(x, int)]
tree.xpath
a[text()='Example']
0
join([(str(k) + ' ' + str(v)) for k, v in list(a.items())])
print(set(re.sub('[\x00-\x7f]', '', '\xa3\u20ac\xa3\u20ac')))
print(re.sub('[\x00-\x7f]', '', '\xa3100 is worth more than \u20ac100'))
ast.literal_eval
print(t.decode('unicode_escape'))
print(str.encode('cp1252').decode('utf-8').encode('cp1252').decode('utf-8'))
zip(list_a, list_b)
list(zip(a, b))
df.set_index('id').to_dict()
df.set_index('id')['value'].to_dict()
re.sub('\\([^)]*\\)', '', filename)
replace(' ', '').isalpha()
x + y
y in zip(first, second)
list(a_dict.items())
key=lambda item: item[1][1]
list(range(len(a)))
key=lambda i: a[i]
-2
zip(*sorted(enumerate(a), key=operator.itemgetter(1)))[0][-2:]
list(range(len(a)))
key=lambda i: a[i]
reverse=True
2
list(x.keys()).index('c')
print('{0:+d}'.format(score))
k for k, g in itertools.groupby([1, 2, 2, 3, 2, 2, 4])
0
1
2
split(',')
int(x) for x in '0,1,2'.split(',')
dict([('A', 1), ('B', 2), ('C', 3)])
np.savetxt('test.txt', x)
direct_output = subprocess.check_output('ls', shell=True)
df[df.columns - ['T1_V6']]
25 < a
a < 100
sum()
date.today().strftime('%A')
car.date_of_manufacture | datetime
car.date_of_manufacture.strftime('%Y-%m-%d')
item for sublist in l for item in sublist
list(itertools.chain(*list2d))
list(itertools.chain.from_iterable(list2d))
ord('a')
re.sub('(?m)^[^\\S\\n]+', '', '  a\n b\n c\nd  e')
re.sub('(?m)^\\s+', '', 'a\n b\n c')
a, b, c = [1, 2, 3]
list(v) for k, v in itertools.groupby
mylist, key=lambda x: x[:5]
line = re.sub('\\(+as .*?\\) ', '', line)
print(line.rstrip('\n'))
df.index.values.tolist()
i for i, v in enumerate(a) if v > 4
sorted(yourdata, reverse=True)
yourdata, key=lambda d: d.get('key', {}).get('subkey'), reverse=True
yourdata.sort
key=lambda e: e['key']['subkey']
reverse=True
df.round()
gca().get_lines()[n].get_xydata()
A[:, -2:]
request.GET.get('username', '')
pprint(dict(list(o.items())))
url('^$', include('sms.urls'))
url('^', include('sms.urls'))
max_item = max(a_list, key=operator.itemgetter(1))
max(a_list, key=operator.itemgetter(1))
s.resample('3M', how='sum')
a[i] for i in (1, 2, 5)
line for line in open('textfile') if 'apple' in line
datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ')
pandas.read_csv(filename, sep='\t', lineterminator='\r')
replace('TEST', '?', 1)
archive.write(pdffile, os.path.basename(pdffile))
dict(x[1:] for x in reversed(myListOfTuples))
x1 - x2
x2 in zip(List1, List2)
string[0].isdigit()
strg.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))
print(os.path.dirname(os.path.realpath(__file__)))
re.split('(?<=\\?|!|\\.)\\s{0,2}(?=[A-Z]|$)', text)
plt.scatter(*zip(*li))
tuple(zip(*t))
df.groupby(np.arange(len(df.columns)) // 3, axis=1).mean()
join(chr(i) for i in L)
sum(x == chosen_value for x in list(d.values()))
sum(1 for x in list(d.values()) if some_condition(x))
struct.unpack('f', struct.pack('f', 0.00582811585976))
timestamp = (dt - datetime(1970, 1, 1)).total_seconds()
df.sort('m')
a = sorted
a, key=lambda x: x.modified, reverse=True
print(bool(a))
df = df.rename(index={last: 'a'})
km.fit(x.reshape(-1, 1))
words, key=lambda x: 'a' + x if x.startswith('s') else 'b' + x
webbrowser.open('http://somesite.com/adminpanel/index.php')
dict((k, v) for k, v in parent_dict.items() if 2 < k < 4)
dict((k, v) for k, v in parent_dict.items() if k > 2 and k < 4)
list(x) for x in zip
zip(list1, list2)
key=lambda pair: pair[0]
sum(((i > 5) for i in j))
len([1 for i in j if (i > 5)])
x + tuple(y)
y in zip(zip(a, b), c)
os.chmod(path, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
parser.add_argument('file', nargs='*')
z = [(i == j) for i, j in zip(x, y)]
x[i] == y[i]
i in range(len(x))
df2 = pd.DataFrame(index=df1.index)
struct.unpack('h', pS[0:2])
print('\n'.join('  '.join(map(str, row)) for row in t))
driver.find_element_by_name('<check_box_name>').is_selected()
driver.find_element_by_id('<check_box_id>').is_selected()
a if a else 2
a in [0, 1, 0, 3]
encode().decode('unicode-escape')
decode('unicode-escape')
chr(int('fd9b', 16)).encode('utf-8')
print('0x%X' % value)
cleaned = [x for x in your_list if x]
slice(*[(int(i.strip()) if i else None) for i in string_slice.split(':')])
soup.find_all(['a', 'div'])
print(func.__name__)
join('{}{}'.format(key, val) for key, val in sorted(adict.items()))
join('{}{}'.format(key, val) for key, val in list(adict.items()))
new_list = old_list[:]
new_list = list(old_list)
new_list = copy.copy(old_list)
new_list = copy.deepcopy(old_list)
i for i in old_list
plt.legend(frameon=False)
encode('utf-16', 'surrogatepass').decode('utf-16')
globals
urllib.request.urlopen('http://www.stackoverflow.com').getcode()
print(urllib.request.urlopen('http://www.stackoverflow.com').getcode())
driver.find_element_by_css_selector
href^='javascript'
click()
df.to_pickle(file_name)
df.groupby(by=df.columns, axis=1).mean()
bar.sort
key=lambda x: (x.attrb1, x.attrb2)
reverse=True
alpha = img.split()[-1]
soup.findAll('div', style='width=300px;')
cursor.execute(sql, list(myDict.values()))
df.to_csv('Result.csv', index=False, sep=' ')
globals
update(vars(args))
re.findall('\\[(.*?)\\]', mystring)
print('%.2f kg = %.2f lb = %.2f gal = %.2f l' % (var1, var2, var3, var4))
d = dict((k, v) for k, v in d.items() if v > 0)
d = {k: v for k, v in list(d.items()) if v > 0}
pd.to_datetime(pd.Series(date_stngs))
df.iloc[2, 0]
matplotlib.rcParams.update({'font.size': 22})
pd.DataFrame(list(d.items()), columns=['Date', 'DateValue'])
pd.DataFrame(df.values * df2.values, columns=df.columns, index=df.index)
re.findall('\\d+\\.\\d+', 'Current Level: 13.4 db.')
re.findall('[-+]?\\d*\\.\\d+|\\d+', 'Current Level: -13.2 db or 14.2 or 3')
zip(it, it, it)
df['x'].str.lower()
jsobj['a']['b']['e'].append({'f': var6, 'g': var7, 'h': var8})
join(lst)
sum(v for v in list(d.values()) if v > 0)
app.run(debug=True)
df.drop(df.index[[1, 3]], inplace=True)
df.apply(lambda x: x.fillna(x.mean()), axis=0)
o.my_attr for o in my_list
time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(file)))
all(item in list(superset.items()) for item in list(subset.items()))
str(wi) for wi in wordids
df2 = df.reset_index()
dt.strftime('%m/%d/%Y')
print('Total cost is: ${:,.2f}'.format(TotalAmount))
df.groupby(np.arange(len(df.columns)) // 2 + 1, axis=1).sum().add_prefix('s')
randomList = [random.random() for _ in range(10)]
print(soup.find('a', href=re.compile('.*follow\\?page.*')))
sys.stdout.flush()
country, capital = random.choice(list(d.items()))
list('Word to Split')
w for w in open('file.txt') if not re.search('[aeiou]{2}', w)
pat = re.compile('^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$')
exec(compile(open('filename.py').read(), 'filename.py', 'exec'))
session.query(Tag).distinct(Tag.name).group_by(Tag.name).count()
df = df.dropna(axis=1, how='all')
all(x.count(1) == 3 for x in L)
x[0] for x in l1 if any(x[0] == y[0] for y in l2)
tex.delete('1.0', END)
datetime.datetime.fromtimestamp(myNumber).strftime('%Y-%m-%d %H:%M:%S')
system('python myscript.py')
your_list.sort(key=operator.attrgetter('anniversary_score'))
your_list.sort
key=lambda x: x.anniversary_score
print(type(tf.Session().run(tf.constant([1, 2, 3]))))
list(itertools.chain(*a))
count.setdefault('a', 0)
df.groupby(['cluster']).mean()
myList, key=lambda x: abs(x - myNumber)
any(x in string for x in search)
print(pattern.search(url).group(1))
s.factorize()[0] + 1
astype('float')
C = [(a - b) for a, b in zip(A, B)]
datetime.datetime.strptime('2011, 4, 0', '%Y, %U, %w')
map(int, ['1', '-1', '1'])
datetime.datetime.strptime('16Sep2012', '%d%b%Y')
Book.objects.filter(pk=pk).update(**d)
Book.objects.create(**d)
print('{0:.2f}'.format(your_number))
random.randint(100000000000, 999999999999)
int(''.join(str(random.randint(0, 9)) for _ in range(12)))
join(str(random.randint(0, 9)) for _ in range(12))
0.12
random.randint(0, 999999999999)
numpy.delete(a, index)
trial_list, key=lambda x: trial_dict[x]
sys.stdin.read(1)
print(re.findall(pattern, x))
k = soup.find(text=re.compile('My keywords')).parent.text
df.apply(lambda x: x.tolist(), axis=1)
B = np.reshape(A, (-1, 2))
app.run(host='192.168.0.58', port=9000, debug=False)
print('\xc5\xc4\xd6'.encode('UTF8'))
x[0] for x in G
re.findall('-(?!aa-|bb-)([^-]+)', string)
re.findall('-(?!aa|bb)([^-]+)', string)
k: v
v in list(hand.items()) 
dict((k, v) for k, v in hand.items() if v)
sorted(L, key=operator.itemgetter('resultType'))
s.sort(key=operator.attrgetter('resultType'))
somelist.sort
key=lambda x: x.resultType
df1.merge(df2, on='name').merge(df3, on='name')
decimal.Decimal(random.randrange(10000)) / 100
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(glob.glob('/home/adam/*.txt'))
os.listdir('somedirectory')
cur.executemany('INSERT INTO table VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)', tup)
print([key for key in d if d[key] == 1])
print([key for key, value in d.items() if value == 1])
print([key for key, value in list(d.items()) if value == 1])
strs = ['' for x in range(size)]
dict(t) for t in set([tuple(d.items()) for d in l])
TIME_ZONE = 'Europe/Istanbul'
dates_dict.setdefault(key, []).append(date)
Article.objects.values('pub_date').annotate(article_count=Count('title'))
canvas.delete('all')
s = pd.Series(['A', 'B', 'A1R', 'B2', 'AABB4'])
a.sort
key=lambda x: b.index(x[0])
plt.savefig('filename.png')
plt.savefig('filename.png', dpi=300)
p1.communicate()[0]
soup.body.findAll(text='Python')
soup.body.findAll(text='Python Jobs')
list(d.items())
key=lambda name_num: (name_num[0].rsplit(None, 1)[0], name_num[1])
set([1, 2, 3]) ^ set([3, 4, 5])
request.POST.getlist('pass_id')
list(dict((x['id'], x) for x in L).values())
df.groupby(df.columns, axis=1).sum()
dict(zip(list(range(1, 5)), list(range(7, 11))))
numpy.where(mask)
string1.lower() == string2.lower()
first.lower() == second.lower()
first.upper() == second.upper()
os.system
10
11
test.txt > test2.txt
del my_list[2:6]
int(s.encode('hex'), 16)
re.findall('TAA(?:[ATGC]{3})+?TAA', seq)
sorted(s, key=float)
hex(65)
a.append(b).reset_index(drop=True)
pd.concat([a, b], ignore_index=True)
i in range(1, 3) for j in range(1, 5)
sorted(iter(mydict.items()), key=itemgetter(1), reverse=True)
pd.date_range('1/1/2014', periods=12, freq='BM')
requests.get('https://kennethreitz.com', verify=False)
df.ix[:-1]
string.find('substring')
pd.concat([df.head(1), df.tail(1)])
MyModel.objects.extra(where=['CHAR_LENGTH(text) > 254'])
MyModel.objects.filter(text__regex='^.{254}.*')
sum(df.apply(lambda x: sum(x.isnull().values), axis=1) > 0)
canvas.create_text(x, y, font=('Purisa', 12), text=k)
y['baz'] for x in foos for y in x['bar']
df = pd.read_csv
comma.csv
quotechar=""
df['a'] = df['a'].str.replace('in.', ' in. ')
i for i in range(len(a)) if a[i] > 2
locals()
globals
hasattr(obj, 'attr_name')
lambda x, y: x + y
sum(1 for i in it)
lst2[i]
x in enumerate(lst)
j in zip(lst, lst2)
lst[i]
lst2[i]
i in range(len(lst))
struct.unpack('BBB', rgbstr.decode('hex'))
3 not in [2, 3, 4]
2
3
not in 
2
3
5
6
9
1
2
3
not in 
2
7
7
3
3 not in [4, 5, 6]
value for pair in zip(a, b[::-1]) for value in pair
b = np.delete(a, -1, 1)
dbb.commit()
pd.merge(a, b, on=['A', 'B'], how='outer')
setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
sum(l) / float(len(l))
v in D.items() 
k = hashlib.md5('thecakeisalie').hexdigest()
birthdays.sort
key=lambda d: (d.month, d.day)
td.findNext(text=True) for td in tr.findAll('td')
tr in rows
Boat.txt.txt
replace('.txt', '')
list(df.index)
df.index
join(list(OrderedDict.fromkeys('aaabcabccd').keys()))
list(set('aaabcabccd'))
df.loc[(df.loc[:, (df.dtypes != object)] != 0).any(1)]
all(word in d for word in ['somekey', 'someotherkey', 'somekeyggg'])
subprocess.check_output(['espeak', text], stderr=subprocess.STDOUT)
df.fillna(method='ffill', inplace=True)
print(np.linspace(1, 3, num=4, endpoint=False))
print(np.linspace(1, 3, num=5))
kdll.CreateSymbolicLinkW('D:\\testdirLink', 'D:\\testdir', 1)
slice = [arr[i][0:2] for i in range(0, 2)]
upload_url = blobstore.create_upload_url('/upload', gs_bucket_name='my_bucket')
os.chdir(os.path.dirname(__file__))
func(*args)
df['AB'].str.split(' ', 1, expand=True)
df['A'], df['B'] = df['AB'].str.split(' ', 1).str
print(sorted(xs, key=len))
xs.sort(lambda x, y: cmp(len(x), len(y)))
xs.sort
key=lambda s: len(s)
ts.plot(marker='.')
lst = list(itertools.product([0, 1], repeat=n))
lst = map(list, itertools.product([0, 1], repeat=n))
lst = list(itertools.product([0, 1], repeat=3))
df['col'] = 'str' + df['col'].astype(str)
dict((name, eval(name)) for name in ['some', 'list', 'of', 'vars'])
plt.colorbar(im, ax=ax)
a for c in Cards for b in c for a in b
sorted(d, key=d.get)
print(len([x for x in lst if x is not None]))
json.key1
mynewlist = list(myset)
set(['a', 'b', 'c', 'd'])
figure(figsize=(11.69, 8.27))
url.rsplit('/', 1)
url.rsplit('/', 1)[-1]
x_file = open(os.path.join(direct, '5_1.txt'), 'r')
list('5+6')
np.concatenate(input_list).ravel().tolist()
print([y for x in list(dict.items()) for y in x])
y for x in list(dict.items()) for y in x
MyModel.objects.order_by('?').first()
os.chdir('chapter3')
os.chdir('C:\\Users\\username\\Desktop\\headfirstpython\\chapter3')
os.chdir('.\\chapter3')
dict((key, sum(d[key] for d in dictList)) for key in dictList[0])
df.sort(['c1', 'c2'], ascending=[True, True])
floats = [float(x) for x in s.split()]
floats = map(float, s.split())
plt.xticks([1, 2, 3, 4, 5])
list(d.values())
iter(d.values())
super(Instructor, self).__init__(name, year)
dict(zip(x, y))
a, key=lambda i: list(i.values())[0], reverse=True
sorted(a, key=dict.values, reverse=True)
df.groupby(level=0).agg(['sum', 'count', 'std'])
a.setdefault('somekey', []).append('bob')
sum(item['gold'] for item in example_list)
sum([item['gold'] for item in example_list])
sum(item['gold'] for item in myLIst)
f.write('text to write\n')
file.write('My String\n')
df.reset_index().groupby('A')['index'].apply(np.array)
fn = os.path.join(os.path.dirname(__file__), 'my_file')
e = next(iter(s))
os.system('dir c:\\')
self.treeview.connect('size-allocate', self.treeview_changed)
3 in [1, 2, 3]
datetime.datetime.strptime('10/05/2012', '%d/%m/%Y').strftime('%Y-%m-%d')
s = s.replace('\\', '\\\\')
print(proc.communicate()[0])
pd.concat([pd.DataFrame(l) for l in my_list], axis=1).T
df.loc[:, ((df != 0).any(axis=0))]
a, key=lambda x: x[1]
x.strip() for x in s.split(',')
items = [item for item in container if item.attribute == value]
open('filename', 'w').write('\n'.join('%s %s' % x for x in mylist))
pattern = re.compile('(?:review: )?(http://url.com/(\\d+))\\s?', re.IGNORECASE)
str = open('very_Important.txt', 'r').read()
df.groupby(['A', 'B'])['C'].unique()
lines = [line.rstrip('\n') for line in open('filename')]
df['col'] = pd.to_datetime(df['col'])
k for d in list(foo.values()) for k in d
print('Hello, {0}, how do you do?'.format(input('Enter name here: ')))
df = pd.read_csv('filename.txt', sep=';', names=['Region Name'])
platform.system()
a = sorted
a, key=lambda x: float(x)
re.search('name (.*)', s)
db.collection.find({}, {'_id': False})
row[1] for row in A
row[0] for row in a
sorted(['10', '3', '2'], key=int)
os.path.commonprefix(['/the/dir/', os.path.realpath(filename)]) == '/the/dir/'
any(substring in string for substring in substring_list)
df = pandas.DataFrame(data, columns=['R_Number', 'C_Number', 'Avg', 'Std'])
re.sub('^((?:(?!cat).)*cat(?:(?!cat).)*)cat', '\\1Bull', s)
re.sub('^((.*?cat.*?){1})cat', '\\1Bull', s)
the_list, key=lambda k: int(k.split('_')[1])
the_list, key=lambda x: int(x.split('_')[1])
list(g) for _, g in itertools.groupby(test, lambda x: x.split('_')[0])
driver.get('http://www.google.com')
datetime.datetime.utcnow() - datetime.timedelta(hours=11)
Counter([1, 2, 2, 2, 3]) - Counter([1, 2])
re.sub('<[^>]*>', '', mystring)
data.encode('hex')
User.objects.filter(userprofile__level__gte=0)
soup.findAll(id=re.compile('para$'))
soup.select('div[id^=""value_xxx_c_1_f_8_a_""]')
cleaned_list = [x for x in some_list if x is not thing]
var = input('Please enter something: ')
foo.append(4)
foo.append([8, 7])
x.insert(2, 77)
plt.savefig('test.png', bbox_inches='tight')
listone + listtwo
males = df[(df[Gender] == 'Male') & (df[Year] == 2014)]
print('\\')
df.replace('-', np.nan)
df = df.drop('column_name', 1)
df.drop(df.columns[[0, 1, 3]], axis=1)
df.drop('column_name', axis=1, inplace=True)
parser = argparse.ArgumentParser(allow_abbrev=False)
feature3 = [d.get('Feature3') for d in df.dic]
df.loc[gb.groups['foo'], ('A', 'B')]
print('[%s, %s, %s]' % (1, 2, 3))
print('[{0}, {1}, {2}]'.format(1, 2, 3))
v for k, v in list(my_dict.items()) if 'Date' in k
df.drop(('col1', 'a'), axis=1)
df.drop('a', level=1, axis=1)
_key: _value
_key in _container
browser.find_element_by_class_name('section-select-all').click()
dict((k, d.get(k, '') + d1.get(k, '')) for k in keys)
hash(pformat(a)) == hash(pformat(b))
list(map(tuple, [['tom', 'cat'], ['jerry', 'mouse'], ['spark', 'dog']]))
df.groupby(['stock', 'same1', 'same2'], as_index=False)['positions'].sum()
s.upper()
dict(item.split('=') for item in s.split(';'))
br.addheaders = [('Cookie', 'cookiename=cookie value')]
df['value'] = df['value'].str[0]
df['value'] = df['value'].str.get(0)
df['value'] = df['value'].str.strip('[]')
join(['{}_{}'.format(k, v) for k, v in d.items()])
sum(sum(x) for x in lists)
any(np.equal(a, [1, 2]).all(1))
len(set(mylist)) == 1
map(int, x.split('\t')) for x in s.rstrip().split('\r\n')
t = sorted
list(a.items())
key=lambda x: x[1]
string2.replace('', string1)[len(string1):-len(string1)]
list(itertools.combinations([1, 2, 3, 4, 5, 6], 2))
x = {}
format(x.decode('utf8')).encode('utf8')
isinstance(x, int)
type(x) == int
winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
next(it) for _ in range(n)
list(itertools.islice(it, 0, n, 1))
set(a).intersection(b)
print(''.join(map(str, data)))
re.match('\\$[0-9]+[^\\$]*$', '$1 off delicious $5 ham.')
importlib.import_module
a.b
importlib.import_module
a.b.c
a = np.array(a)
soup.find_all('div', class_=re.compile('comment-'))
_ in range(n)
dict((k, globals()[k]) for k in ('foo', 'bar'))
MyModel.objects.order_by('?')[:2]
user[name]
format(**{'user': {'name': 'Markus'}})
t[0]
t for t in tuple_list
randint(0, 9)
random.randint(a, b)
print((random.randint(0, 9)))
join(reversed([a[i:i + 2] for i in range(0, len(a), 2)]))
pd.pivot_table(df, index=df.index.date, columns=df.index.time, values='Close')
any(item[2] == 0 for item in items)
x for x in items if x[2] == 0
list(dic.items())
key=lambda x: x[1]['Fisher']
reverse=True
plt.yscale('log', nonposy='clip')
os.listdir('/home/username/www/')
os.listdir('path')
pd.concat([distancesDF, datesDF.dates], axis=1)
x[0] for x in a
i[0] for i in a
re.sub('(?<=[a-z])\\r?\\n', ' ', textblock)
gzip.open('file.gz', 'rt', encoding='utf-8')
set(['a', 'b']).issubset(['b', 'a', 'foo', 'bar'])
all(x in ['b', 'a', 'foo', 'bar'] for x in ['a', 'b'])
line.translate(None, '!@#$')
line = re.sub('[!@#$]', '', line)
string.replace('1', '')
a = a.replace(char, '')
a = a.replace(char, '')
line = line.translate(string.maketrans('', ''), '!@#$')
pd.concat([df, pd.get_dummies(df, '', '').astype(int)], axis=1)[order]
3
4
1
2
globals
re.sub('([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))', '\\1 ', text)
print('ex\xe1mple'.upper())
l.split('\\')[-1] for l in list_dirs
dict(zip(keys, values))
formatter = logging.Formatter('%(asctime)s;%(levelname)s;%(message)s')
new_string = re.sub('""(\\d+),(\\d+)""', '\\1.\\2', original_string)
subprocess.call('test.sh otherfunc')
join(foo.split())
list('{0:0b}'.format(8))
int(x) for x in list('{0:0b}'.format(8))
int(x) for x in bin(8)[2:]
dict(zip(my_list, map(my_dictionary.get, my_list)))
numpy.dstack(numpy.meshgrid(x, y)).reshape(-1, 2)
driver.implicitly_wait(60)
driver.switch_to_frame('frameName')
time.strftime('{%Y-%m-%d %H:%M:%S}')
sorted(['14:10:01', '03:12:08'])
re.findall('(?:\\w+(?:\\s+\\w+)*,\\s)+(?:\\w+(?:\\s\\w+)*)', x)
df1.groupby(['key', 'year']).size().reset_index()
sorted(list(dictionary.items()), key=operator.itemgetter(1))
iter(d.items())
key=lambda x: x[1]
list(dictionary.items())
key=lambda x: x[1]
np.split(a, [-1])
df.pivot(index='order', columns='sample')
df[(df['A'] > 1) | (df['B'] < -1)]
list(a) for a in zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(df.loc[df['A'] == 'foo'])
df.loc[df['column_name'] != some_value]
df.loc
df['column_name'].isin(some_values)
df.loc[df['column_name'] == some_value]
print(df.loc[df['B'].isin(['one', 'three'])])
join(map(lambda x: x * 7, 'map'))
os.rmdir()
shutil.rmtree(path, ignore_errors=False, onerror=None)
os.removedirs(name)
df.loc[len(df)] = ['8/19/2014', 'Jun', 'Fly', '98765']
glob.glob('*')
glob.glob('[!hello]*.txt')
glob.glob('hello*.txt')
eval('20<30')
new_list = [x[:] for x in old_list]
50
format(float(a[0] / a[1]))
df.to_sparse(0)
print([obj.attr for obj in my_list_of_objs])
sum(1 if d['success'] else 0 for d in s)
sum(d['success'] for d in s)
imp.find_module('os')[1]
bool(a) != bool(b)
a and (not b)
or ((not a) and b)
bool(a) ^ bool(b)
xor(bool(a), bool(b))
return (bool(str1) ^ bool(str2))
my_list.sort(key=operator.itemgetter('name'))
re.split('\\s*,\\s*|\\s*;\\s*', 'a , b; cdf')
t.strip() for s in string.split(',') for t in s.split(';')
f = lambda x, y: x + y
instancelist = [MyClass() for i in range(29)]
f[i + 1]
f[i]
f[i + 2]
i in range(0, len(f), 3)
struct.unpack('>q', s)[0]
pd.concat([students, pd.DataFrame(marks)], axis=1)
alist.sort
key=lambda x: x.foo
soup.select('div[id$=_answer]')
linsolve(Matrix(([1, 1, 1, 1], [1, 1, 2, 3])), (x, y, z))
k: bigdict[k] 
k in list(bigdict.keys()) & {'l', 'm', 'n'}
dict((k, bigdict[k]) for k in ('l', 'm', 'n'))
k: bigdict
get(k, None) for k in ('l', 'm', 'n')
k: bigdict[k] 
k in ('l', 'm', 'n')
driver.page_source
data[:, ([1, 9])]
re.sub('\\[.*?\\]', '', 'abcd[e]yth[ac]ytwec')
re.findall('\\b(?:b+a)+b+\\b', mystring)
str_list = [tuple('{0:.8e}'.format(flt) for flt in sublist) for sublist in lst]
str_list = [['{0:.8e}'.format(flt) for flt in sublist] for sublist in lst]
t = tuple(x[0] for x in s)
datetime.datetime.now().strftime('%a')
ord('a')
ord('\u3042')
ord()
json.load(u)
yourdf.drop(['columnheading1', 'columnheading2'], axis=1, inplace=True)
s.strip() for s in input().split(',')
int(d) for d in str(bin(x))[2:]
max(len(word) for word in i)
len(max(i, key=len))
os.system(my_cmd)
mylist.sort
key=lambda x: x.lower()
mylist.sort(key=str.lower)
mylist.sort()
list.sort()
df.set_index(['Company', 'date'], inplace=True)
getattr(your_obj, x)
s.split(' ', 1)[1]
workbook = xlsxwriter.Workbook('app/smth1/smth2/Expenses01.xlsx')
workbook = xlsxwriter.Workbook('C:/Users/Steven/Documents/demo.xlsx')
pyplot.legend(loc=2, fontsize='x-small')
plot.legend(loc=2, prop={'size': 6})
l[i:i + n] for i in range(0, len(l), n)
l[i:i + n] for i in range(0, len(l), n)
df['a'].str.contains('-')
re.sub
it -technically- works
print(re.findall('\\d+', '\n'.join(re.findall('\xab([\\s\\S]*?)\xbb', text))))
monthly_mean.reset_index().plot(x='index', y='A')
subprocess.check_output('echo ""foo""', shell=True)
x.encode('UTF8') for x in EmployeeList
pandas.concat([df['foo'].dropna(), df['bar'].dropna()]).reindex_like(df)
list(range(9))
join(chr(i) for i in myintegers)
super(Executive, self).__init__(*args)
item for item in my_sequence if item != 'item'
random.choice(foo)
set(['a', 'b']).issubset(['a', 'b', 'c'])
set(['a', 'b']).issubset(set(l))
list(t) for t in zip(*list_of_tuples)
zip(*list_of_tuples)
pd.merge(y, x, on='k')[['a', 'b', 'y']]
item.strip() for item in my_string.split(',')
print((obj.__dict__))
dir()
dir()
window.set_position(Gtk.WindowPosition.CENTER)
plt.rc('font', **{'size': '30'})
df.isnull().values.any()
some_func(*params)
urllib.parse.unquote(h.path.encode('utf-8')).decode('utf-8')
trace_df['ratio'] > 0
mean()
emaillist = '\n'.join(item[0] for item in queryresult)
item[0] for item in queryresult
emaillist = '\n'.join([item[0] for item in queryresult])
print(('focus object class:', window2.focus_get().__class__))
a = [0] * 10000
print(' '.join(sorted(set(words), key=words.index)))
random.sample(range(1, 50), 6)
random.sample(range(1, 50), 6)
k.lower()
v.lower() for k, v in list({'My Key': 'My Value'}.items())
dict((k.lower(), v) for k, v in {'My Key': 'My Value'}.items())
dict((k.lower(), v.lower()) for k, v in {'My Key': 'My Value'}.items())
sorted(item) for item in data
names = list(map(lambda x: x[0], cursor.description))
os.path.abspath(__file__)
sorted(matrix, key=itemgetter(1))
index for index, letter in enumerate(word) if letter == 'e'
print(str(x).decode('raw_unicode_escape'))
re.findall('\\w', 'abcdefg')
os.path.isfile(fname)
os.path.exists(file_path)
print(os.path.isfile('/etc/password.txt'))
print(os.path.isfile('/etc'))
print(os.path.exists('/does/not/exist'))
print(os.path.isfile('/does/not/exist'))
print(os.path.exists('/etc'))
print(os.path.exists('/etc/password.txt'))
replace(';', ' ').replace(',', ' ').split()
list(i for i in range(3))
writer.writeheader()
0
0
08
format(3652458)
v in list(d.items())
v in d.items()
v in a.items()
v in a.items()
int(x, 16) for x in ['BB', 'A7', 'F6', '9E']
int(x, 16) for x in L
var1, var2 = input('Enter two numbers here: ').split()
Test.objects.filter(actions__contains=[{'fixed_key_1': 'foo2'}])
itertools.product(list(range(2)), repeat=4)
datetime.now() - timedelta(1)
strftime('%Y-%m-%d')
np.dot([1, 0, 0, 1, 0, 0], [[0, 1], [1, 1], [1, 0], [1, 0], [1, 1], [0, 1]])
df['date'] = pd.to_datetime(df['date'], format='%d%b%Y')
x.reset_index().merge(y, how='left', on='state', sort=False).sort('index')
json.loads(request.POST.get('mydata', '{}'))
list(zip(*((iter([1, 2, 3, 4, 5, 6, 7, 8, 9]),) * 3)))
list(grouper(2, [1, 2, 3, 4, 5, 6, 7]))
keys.sort
key=lambda x: map(int, x.split('.'))
keys.sort
key=lambda x: [int(y) for y in x.split('.')]
img.transpose(2, 0, 1).reshape(3, -1)
df['BrandName'].replace(['ABC', 'AB'], 'A')
df['BrandName'] = df['BrandName'].replace(['ABC', 'AB'], 'A')
df.sub(df.mean(axis=1), axis=0)
join([i for i in s if i.isalpha()])
l = (int(x) for x in s.split())
42
0
split()
i for i, elem in enumerate(bool_list, 1) if elem
data.groupby(data['date'].map(lambda x: x.year))
np.in1d(b, a).nonzero()[0]
time.strftime('%l:%M%p %z on %b %d, %Y')
ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=45)
join(['x', 'x', 'x'])
np.arange(x.shape[0]) != 1
print(item['name'])
result = sys.stdin.read()
join(soup.findAll(text=True))
data[data['Value'] == True]
join(set(foo))
Profile.objects.all()
key=lambda p: p.reputation
df.values.flatten()
users.sort
key=lambda x: order.index(x['id'])
users.sort
key=lambda x: order.index(x['id'])
r = requests.get('<MY_URI>', headers={'Authorization': 'TOK:<MY_TOKEN>'})
print('""Hello,\\nworld!""'.decode('string_escape'))
re.findall('a*?bc*?', 'aabcc', re.DOTALL)
a.shape[1]
d.apply(lambda row: min([row['A'], row['B']]) - row['C'], axis=1)
count('ab')
d['key'] for d in l if 'key' in d
d['key'] for d in l
d['key'] for d in l
l1.sort
key=lambda x: int(x[0])
sorted([[1, 'mike'], [1, 'bob']])
translate(maketrans('abcABC', 'defDEF'))
join([('%s:: %s' % (key, value)) for key, value in list(d.items())])
os.system('cls')
os.system('clear')
os.system('tcsh your_own_script')
os.system
zsh -c
0
dict(d, count=n) for d, n in zip(l1, l2)
sum(x) for x in zip(*l)
map(sum, zip(*l))
np.count_nonzero
np.isnan(data)
map(list, zip(*main_list))
request.POST.get('title', '')
test.mp3
endswith(('.mp3', '.avi'))
re.findall('\\[[^\\]]*\\]|""[^""]*""|\\S+', s)
data.apply(lambda x: sorted(x, 3))
os.chdir('C:/Users/Name/Desktop')
re.findall('\\$([^$]*)\\$', string)
re.findall('\\$(.*?)\\$', '$sin (x)$ is an function of x')
datetime.datetime.strptime(str_date, '%m/%d/%Y').date().isoformat()
A[[0, 1], [0, 1]]
a[np.arange(3), (0, 1, 0)]
k for k, v in dictA.items() if v.count('duck') > 1
2
3
4
2
3
4
2
3
4
print(arr[1, 1])
quadmesh.set_clim(vmin=0, vmax=15)
my_data = genfromtxt('my_file.csv', delimiter=',')
df = pd.read_csv('myfile.csv', sep=',', header=None)
np.genfromtxt('myfile.csv', delimiter=',')
np.genfromtxt('myfile.csv', delimiter=',', dtype=None)
my_string.splitlines()[0]
df.values.tolist()
re.sub('\\*\\*+', '*', text)
re.sub('\\*+', '*', text)
dict((k, v * dict2[k]) for k, v in list(dict1.items()) if k in dict2)
return ''.join(random.choice(string.lowercase) for i in range(length))
sum(len(x) for x in list(food_colors.values()))
sum(len(v) for v in food_colors.values())
all(a_list)
join(c for c in text if c not in 'aeiouAEIOU')
x / y
y in zip(a, b)
re.findall('abc(de)fg(123)', 'abcdefg123 and again abcdefg123')
df.groupby('type').apply(lambda x: np.mean(np.log2(x['v'])))
key for key, value in list(my_dict.items()) if set(value).intersection(lst)
key for item in lst for key, value in list(my_dict.items()) if item in value
c = [[(i + j) for i, j in zip(e, b)] for e in a]
os.path.commonprefix(['/usr/var', '/usr/var2/log'])
print(os.path.relpath('/usr/var/log/', '/usr/var'))
grouped.filter(lambda x: len(x) > 1)
list(myDict.items())
key=lambda e: e[1][2]
format(name='john')
df.reindex(['Z', 'C', 'A'])
any(isinstance(el, list) for el in input_list)
len(items)
len([1, 2, 3])
items.__len__()
len()
len(s)
df.sort(axis=1, ascending=False)
df.groupby(['col5', 'col2']).size().groupby(level=1).max()
mydict.pop('key', None)
del mydict[key
parser.add_argument('input', nargs='+')
pyplot.plot(x, y, color='#112233')
re.sub('<[^<]+?>', '', text)
a[np.in1d(a, b)]
jvm.args= -Dappdynamics.com=true
-Dsomeotherparam=false
split('=', 1)
print('[%s]' % ', '.join('%.3f' % val for val in list))
print('[' + ', '.join('%5.3f' % v for v in l) + ']')
print([('%5.3f' % val) for val in l])
os.chdir('..')
print(text.encode('windows-1252'))
struct.unpack('d', struct.pack('Q', int(s2, 0)))[0]
float(int('-0b1110', 0))
struct.unpack('d', b8)[0]
df.colour.value_counts().plot(kind='bar')
df.groupby('colour').size().plot(kind='bar')
line.strip().split(' ')
df.groupby(lambda idx: 0).agg(['mean', 'std'])
list(tag_weight.items())
key=lambda x: int(x[1])
reverse=True
int(math.ceil(x)) - 1
it = iter(sorted(d.items()))
return sorted(dict.items())
return iter(sorted(dict.items()))
last = len(s) - s[::-1].index(x) - 1
str1 = ''.join(list1)
join((str(x) for x in L))
str1 = ''.join((str(e) for e in list1))
makeitastring = ''.join(map(str, L))
x for x in L if x is not None
random.choice([1, 2, 3])
x = [[None for _ in range(5)] for _ in range(6)]
A[(np.random.choice(A.shape[0], 2, replace=False)), :]
A[(np.random.randint(A.shape[0], size=2)), :]
df.groupby(df.index).sum()
root.findall('{http://www.w3.org/2002/07/owl#}Class')
join(random.choice(string.lowercase) for x in range(X))
sys.path.append('/path/to/2014_07_13_test')
int(round(x))
h = int(round(h))
round(32.268907563, 3)
round(value, significantDigit)
round(1.0005, 3)
round(2.0005, 3)
round(3.0005, 3)
round(4.0005, 3)
round(8.005, 2)
round(7.005, 2)
round(6.005, 2)
round(1.005, 2)
df['Cat1'].fillna(df['Cat2'])
logging.info('date=%s', date)
logging.info('date={}'.format(date))
k: int
v in d.items()
map(sum, zip(*lists))
s.decode('hex')
binascii.a2b_hex(s)
connection.send('HTTP/1.0 200 established\r\n\r\n')
connection.send('HTTP/1.0 200 OK\r\n\r\n')
df['x']['C'] = 10
np.sqrt(np.square(df).sum(axis=1))
sorted(set(my_list))
enumerate(a)
key=lambda x: x[1]
0
d['Name'] for d in thisismylist
d['Name']
d['Age']
d in thisismylist
model.objects.all().order_by('?')[0]
os.system('script2.py 1')
re.findall('\\w+(?:-\\w+)+', text)
parser.add_argument('--conf', nargs=2, action='append')
random.sample(list(range(1, 16)), 3)
strings.sort
key=lambda str: re.sub('.*%(.).*', '\\1', str)
strings.sort
key=lambda str: re.sub('.*%', '', str)
listy = [[] for i in range(3)]
A = np.array(sorted(A, key=tuple))
x + y
x in '12345' for y in 'ab'
strip()
myString.strip()
strip()
strip()
strip()
strip()
str.strip()
myString.strip('\n')
myString.lstrip('\n\r')
myString.rstrip('\n\t')
strip(' ')
unsorted, key=lambda element: (element[1], element[2])
print(content.decode('utf8'))
np.ma.array
np.tile(arr, 2).reshape(2, 3)
argmax(axis=1)
pd.to_datetime(df.ID.str[1:-3])
df = pd.read_csv('my.csv', dtype={'my_column': np.float64}, na_values=['n/a'])
df = pd.read_csv('my.csv', na_values=['n/a'])
list(itertools.product(*a))
re.sub('[^A-Z]', '', s)
datetime.strptime('2011221', '%Y%W%w')
codecs.open('myfile', 'r', 'iso-8859-1').read()
f(x) for x in list
re.findall('(?<!\\d)\\d{5}(?!\\d)', s)
item for item in a if sum(item) > 10
cents_int = int(round(float(dollars.strip('$')) * 100))
join(dropwhile(lambda x: x in bad_chars, example_line[::-1]))[::-1]
l = []
l = list()
list()
sys.exit(0)
s[:4] + '-' + s[4:]
i in range(3)
a = [[] for i in range(3)]
requests.get(url, headers={'referer': my_referer})
pylab.ylim([0, 1000])
pd.get_dummies(s.apply(pd.Series).stack()).sum(level=0)
y = str(int(x, 16))
a.isdigit()
isdigit()
b.isdigit()
pd.read_csv(StringIO(s), sep=',', comment='#')
df['Date'] = df['Date'].apply(lambda x: int(str(x)[-4:]))
sum(list_of_nums)
lst, key=lambda x: x['score']
soup.findAll(attrs={'name': 'description'})
str({'a': 1, 'b': 'as df'}).replace(': ', ':').replace(', ', ',')
+ ','.join('{0!r}:{1!r}'.format(*x) for x in list(dct.items())) + '}'
join(parts[1:])
+"""""".join(c.rsplit('+', 1))
a[np.all(a != 0, axis=1)]
join(re.split('[^a-zA-Z]*', 'your string'))
re.split('[^a-zA-Z]*', 'your string')
results_union = set().union(*results_list)
return list(set(itertools.chain(*result_list)))
np.any(np.in1d(a1, a2))
return ''.join(ch for ch in s if unicodedata.category(ch)[0] != 'C')
all(i < j for i, j in zip(a, b))
driver.find_element_by_css_selector('.button.c_button.s_button').click()
os.system('taskkill /im make.exe')
print(select([my_table, func.current_date()]).execute())
re.sub('([a-z])\\1+', '\\1', 'ffffffbbbbbbbqqq')
re.sub('(?<!\\w)([A-Z])\\.', '\\1', s)
split_list = [the_list[i:i + n] for i in range(0, len(the_list), n)]
re.sub('\\b(this|string)\\b', '<markup>\\1</markup>', 'this is my string')
1
pandas.set_option('display.max_columns', 7)
pandas.set_option('display.max_columns', None)
df.ix[df.A == 0, 'B'] = np.nan
driver.find_element_by_xpath
li/label/input
mylist.sort(key=operator.itemgetter('weight', 'factor'))
mylist.sort
key=lambda d: (d['weight'], d['factor'])
x[1]
x for x in lol
d, key=lambda k: d[k][1]
int(round(123, -2))
fd = os.open('x', os.O_WRONLY | os.O_CREAT | os.O_EXCL)
new_list = [x.split()[-1] for x in Original_List]
-1
s[::(-1)]
join(reversed('foo'))
join(reversed(string))
-1
a_string[::(-1)]
join(reversed(s))
join(str(i) for i in range(100) if i % 4 in (1, 2))
dict([(e[0], int(e[1])) for e in lst])
list_of_tuples, key=lambda tup: tup[::-1]
list_of_tuples, key=lambda tup: tup[1]
numpy.concatenate([a, b])
pickle.dump(itemlist, outfile)
outfile.write('\n'.join(itemlist))
session.query(User).filter_by(id=123).update({'name': 'Bob Marley'})
r = requests.post('http://wikipedia.org', cookies=cookie)
sys.path.insert(0, 'libs')
datetime.datetime.now()
datetime.datetime.now().time()
strftime('%Y-%m-%d %H:%M:%S', gmtime())
str(datetime.now())
datetime.datetime.time(datetime.datetime.now())
ord('\xff')
df.groupby(['PplNum', 'RoomNum']).cumcount() + 1
datetime.utcnow()
a[-1:] + a[:-1]
df.set_index(['year', 'month', 'item']).unstack(level=-1)
df.pivot_table(values='value', index=['year', 'month'], columns='item')
print('\n\x1b[4m' + '3' + '\x1b[0m' + '\n2')
range(10, 0, -1)
name[0].firstChild.nodeValue
thread.start_new_thread(myfunction, ('MyStringHere', 1))
thread.start_new_thread(myfunction, ('MyStringHere', 1))
a.index(max(a))
re.sub('\\.(?=[^ .])', '. ', para)
i.split() for i in re.findall('\\[([^\\[\\]]+)\\]', a)
d for d in a if d['name'] == 'pluto'
d for d in a if d['name'] == 'pluto'
list(d.values())
re.sub(' +', ' ', s)
os.chmod('my_script.sh', 484)
df.to_csv('c:\\data\\t.csv', index=False)
re.sub('\\w*\\d\\w*', '', words).strip()
dogtail.rawinput.click(100, 100)
datetime.strptime('2009/05/13 19:19:30 -0400', '%Y/%m/%d %H:%M:%S %z')
re.search('\\bis\\b', String).start()
re.search('is', String).start()
tuple(map(int, input().split(',')))
tuple(int(x.strip()) for x in input().split(','))
str.decode('utf-8').replace('\u2022', '*').encode('utf-8')
str.decode('utf-8').replace('\u2022', '*')
np.zeros((3, 3)).ravel()
print(os.name)
50% sale
0
format('today')
list, key=lambda x: float('inf') if math.isnan(x[1]) else x[1]
a = [(sum(x) / len(x)) for x in zip(*a)]
logging.info('Log message', extra={'app_name': 'myapp'})
df.applymap(lambda x: isinstance(x, (int, float)))
l, key=lambda x: int(re.search('\\d+', x).group(0))
self.root.destroy()
df.iloc[:, ([2, 5, 6, 7, 8])].mean(axis=1)
df[df.index.map(lambda x: x[1].endswith('0630'))]
db.session.delete(page)
join(chr(ord(c)) for c in 'Andr\xc3\xa9')
join(chr(ord(c)) for c in 'Andr\xc3\xa9').decode('utf8')
os.listdir(path)
os.rename(dir, dir + '!')
-"""""".join(a + b for a, b in zip(s[::2], s[1::2]))
print('%.3f' % 3.1415)
data[0]['f'] = var
print(a_module.__file__)
print(os.getcwd())
path = os.path.abspath(amodule.__file__)
self.myList.extend([0] * (4 - len(self.myList)))
df.index.duplicated()
foo(*i)
2
i in range(16)
iter(mydict.items())
key=lambda tup: sum(tup[1])
reverse=True
3
heapq.nlargest
3
iter(mydict.items())
key=lambda tup: sum(tup[1])
index('b')
plt.setp(legend.get_title(), fontsize='xx-small')
x[1] for x in elements
np.diag(np.rot90(array))
list(chain.from_iterable(a))
re.sub('\\s{2,}', '|', line.strip())
print(('%.2f' % a))
print(('{0:.2f}'.format(a)))
print(('{0:.2f}'.format(round(a, 2))))
print(('%.2f' % round(a, 2)))
2
13.9499999
2
3.14159
float('{0:.2f}'.format(13.95))
0
2
format(13.95)
DataFrame.from_csv('c:/~/trainSetRel3.txt', sep='\t')
dateutil.parser.parse('2013/09/11 00:17 +0900')
cur.mogrify('SELECT * FROM table WHERE column IN %s;', ((1, 2, 3),))
sum([sum(x) for x in [[1, 2, 3, 4], [2, 4, 5, 6]]])
next(iter(dict.values()))
next(iter(list(dict.values())))
df.groupby(['Month', 'Fruit']).sum().unstack(level=0)
mylist, key=lambda x: order.index(x[1])
persons, key=lambda x: x['passport']['birth_info']['date']
urlparse.urldefrag('http://www.address.com/something#something')
urllib.request.urlretrieve('http://example.com/file.ext', '/path/to/dir/filename.ext')
list(set(frozenset(item) for item in L))
set(item) for item in set(frozenset(item) for item in L)
p.terminate()
del mylist[:]
ctypes.windll.user32.MessageBoxW(0, 'Error', 'Error', 0)
str_list = list([_f for _f in str_list if _f])
re.sub('[\\ \\n]{2,}', '', yourstring)
re.sub('\\.[^.]+$', '', s)
A[np.all(np.any(A - B[:, (None)], axis=2), axis=0)]
a.to_csv('test.csv', cols=['sum'])
exec(compile(open('test2.py').read(), 'test2.py', 'exec'))
subprocess.call('test1.py', shell=True)
zipped, key=lambda x: x[1]
list(y.items())
key=lambda x: (x[1], x[0])
reverse=True
soup.find_all('div', class_='crBlock ')
element for i, element in enumerate(centroids) if i not in index
list(set(listA) & set(listB))
urllib.request.urlretrieve('http://randomsite.com/file.gz', 'file.gz')
file_name = wget.download(file_url)
ax.set_yticklabels(['\xe9', '\xe3', '\xe2'])
list(itertools.product(list(range(-x, y)), repeat=dim))
print(s.encode('unicode_escape'))
Hello %s
join(my_args)
re.split('(ddd)', 'aaa bbb ccc ddd eee fff', 1)
re.split('(d(d)d)', 'aaa bbb ccc ddd eee fff', 1)
pd.DataFrame(d)
This is a
split()
This     is a
split()
woduplicates = list(set(lseperatedOrblist))
sum([(i * j) for i, j in list(itertools.combinations(l, 2))])
re.compile('{}-\\d*'.format(user))
float(i) for i in lst
writer.writerow(A)
writer.writerows(A)
format('foo', 'bar')
example = [x.replace('\r\n', '') for x in example]
i.partition('\t')[-1] for i in l if '\t' in i
re.search('Test(.*)print', testStr, re.DOTALL)
next = driver.find_element_by_css_selector('li.next>a')
os.stat('C:\\Python27\\Lib\\genericpath.py').st_size
imtag = re.match('<img.*?>', line).group(0)
os.rename('Joe Blow', 'Blow, Joe')
re.findall('(?=(\\w\\w))', 'hello')
bin(173)
int('01010101111', 2)
int('010101', 2)
int('0b0010101010', 2)
bin(21)
int('11111111', 2)
re.sub('$\\d+\\W+|\\b\\d+\\b|\\W+\\d+$', '', s)
re.sub('\\b\\d+\\b', '', s)
s = re.sub('^\\d+\\s|\\s\\d+\\s|\\s\\d+$', ' ', s)
s.split(':', 1)[1]
print(s.split(','))
mystring.split(',')
re.sub('\\((\\w+)\\)', '\\1', s)
webbrowser.open_new(url)
webbrowser.open('http://example.com')
self.pushButton.setStyleSheet('background-color: red')
x(y) for x, y in zip(functions, values)
wx.TextCtrl(self, -1, size=(300, -1))
imshow(imageArray, cmap='Greys_r')
df.fillna(0)
df.toPandas().to_csv('mycsv.csv')
df.write.csv('mycsv.csv')
sum(x[1] for x in structure)
df.groupby('STNAME')['COUNTY_POP'].agg(lambda x: x.nlargest(3).sum())
datetime.strptime('21/11/06 16:30', '%d/%m/%y %H:%M')
os.path.dirname(os.path.abspath(__file__))
re.sub('(.)', '\\1\\1', text.read(), 0, re.S)
join(('a', 'b', 'c', 'd', 'g', 'x', 'r', 'e'))
os.path.dirname(os.path.abspath(__file__))
0
1
format(value, digits)
self.request.url
random_choice = random.choice(choices)
length = sum(len(s) for s in strings)
s = sorted
s, key=lambda x: (x[1], x[2])
s.sort(key=operator.itemgetter(1, 2))
con.commit()
k for k in lst if 'ab' in k
output = ''.join(item[0].upper() for item in input.split())
CustomPK._meta.pk.name
len(s.split())
np.einsum('ji,i->j', a, b)
sys.version
sys.version_info
print('\\num{{{0:.2g}}}'.format(1000000000.0))
x = [[] for i in range(3)]
my_variable | forceescape | linebreaks
zip(*[(1, 4), (2, 5), (3, 6)])
list(group) for key, group in itertools.groupby(data, operator.itemgetter(1))
list('hello')
df['A_perc'] = df['A'] / df['sum']
os.walk(directory)
x[0] for x in os.walk(directory)
j in list(d.items()) 
j != 'None'
dict((k, 'updated') for k, v in d.items() if v is None)
dict((k, 'updated') for k, v in d.items() if v != 'None')
df.groupby(key_columns).size()
result = [sum(b) for b in a]
any(d['site'] == 'Superuser' for d in data)
nodes = [[Node() for j in range(cols)] for i in range(rows)]
print(os.path.splitext('/home/user/somefile.txt')[0] + '.jpg')
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
ax.set_title('$%s \\times 10^{%s}$' % ('3.5', '+20'))
print(os.path.getmtime('/tmp'))
today.strftime('%B')
today.strftime('%B')
j for i in x for j in i
print(list(itertools.chain.from_iterable(a)))
datetime.datetime.strptime('January 11, 2010', '%B %d, %Y').strftime('%A')
a.remove('b')
a.remove(c)
a.remove(6)
a.remove(6)
re.findall('(?=(a.*?a))', 'a 1 a 2 a 3 a 4 a')
np.einsum('ij,kj->jik', X, X)
some_list[(-1)]
some_list[(-2)]
some_list[(- n)]
alist[(-1)]
astr[(-1)]
print([u for v in [[i, i] for i in range(5)] for u in v])
0
0
1
1
2
2
3
3
4
4
i // 2
i in range(10)
s[s.find('\n') + 1:s.rfind('\n')]
x ** 2
x in range(100)
zip(*[[1, 2], [3, 4], [5, 6]])
zip(*[[1, 2], [3, 4], [5, 6]])
requests.get('https://www.mysite.com/', auth=('username', 'pwd'))
x[2:]
x[:2]
x[:(-2)]
x[(-2):]
x[2:(-2)]
some_string[::(-1)]
H-e-l-l-o- -W-o-r-l-d
2
s = s[beginning:(beginning + LENGTH)]
sys.exit()
quit()
sys.exit('some error message')
data['City'].encode('ascii', 'ignore')
pd.read_csv('D:/Temp/tt.csv', names=list('abcdef'))
df.stack().groupby(level=0).first()
0
1
format(10, 20)
1
0
1
format(10, 20, foo='bar', ham='spam')
changed_list = [(int(f) if f.isdigit() else f) for f in original_list]
dict(zip(keys, zip(*data)))
apple.decode('iso-8859-1').encode('utf8')
df.to_csv('filename.csv', header=False)
print('{0}:<15}}{1}:<15}}{2}:<8}}'.format('1', '2', '3'))
ld, key=lambda d: d['size']
0
2
1
2
format('b', 'a')
user = models.ForeignKey('User', unique=True)
re.compile('^([^A]*)AA([^A]|AA)*$')
b = np.concatenate((a, a), axis=0)
l, key=lambda x: x.replace('0', 'Z')
ax.set_yscale('log')
os.environ['HOME']
os.environ['HOME']
print(os.environ)
os.environ
print(os.environ.get('KEY_THAT_MIGHT_EXIST'))
print(os.getenv('KEY_THAT_MIGHT_EXIST', default_value))
print(os.environ.get('HOME', '/home/username/'))
print(dict([s.split('=') for s in my_list]))
enumerate(a)
key=lambda x: abs(x[1] - 11.5)
e = root.xpath('.//a[contains(text(),""TEXT A"")]')
e = root.xpath('.//a[starts-with(text(),""TEXT A"")]')
e = root.xpath('.//a[text()=""TEXT A""]')
c = [b[i] for i in index]
np.dot(a[:, (None)], b[(None), :])
np.outer(a, b)
subprocess.call(['./abc.py', arg1, arg2])
df[['value']].fillna(df.groupby('group').transform('mean'))
re.sub('(.)(?=.)', '\\1-', s)
re.sub('(?<=.)(?=.)', '-', str)
i, j = np.where(a == value)
print(collections.Counter(s).most_common(1)[0])
float(re.findall('(?:^|_)' + par + '(\\d+\\.\\d*)', dir)[0])
re.findall('[^a]', 'abcd')
print([item for item in dir(adfix) if not item.startswith('__')])
x[0] for x in rows
res_list = [x[0] for x in rows]
pd.concat([x] * 5, ignore_index=True)
pd.concat([x] * 5)
sorted_list_of_keyvalues = sorted(list(ips_data.items()), key=item[1]['data_two'])
pd.read_json(elevations)
numpy.random.choice(numpy.arange(1, 7), p=[0.1, 0.05, 0.05, 0.2, 0.4, 0.2])
df.loc[df['Value'].idxmax()]
re.findall('^(.+?)((.+)\\3+)$', '42344343434')[0][:-1]
np.fromstring('\x00\x00\x80?\x00\x00\x00@\x00\x00@@\x00\x00\x80@', dtype='<f4')
np.fromstring('\x00\x00\x80?\x00\x00\x00@\x00\x00@@\x00\x00\x80@', dtype='>f4')
cursor.execute('INSERT INTO table VALUES (?, ?, ?)', (var1, var2, var3))
cursor.execute('INSERT INTO table VALUES (%s, %s, %s)', (var1, var2, var3))
df['stats'].str[1:-1].str.split(',', expand=True).astype(float)
df['stats'].str[1:-1].str.split(',').apply(pd.Series).astype(float)
df['stats'].apply(pd.Series)
p.wait()
s.encode('utf8')
datetime.datetime.strptime('01-Jan-1995', '%d-%b-%Y')
copyfile(src, dst)
shutil.copy2('/dir/file.ext', '/new/dir/newname.ext')
shutil.copy2('/dir/file.ext', '/new/dir')
print(', '.join(str(x) for x in list_of_ints))
df[['A', 'B']].multiply(df['C'], axis='index')
hex(ord('a'))
sum(j ** i for i, j in enumerate(l, 1))
join(s.split())
s = s.replace(',', '')
frame.resample('1H').agg({'radiation': np.sum, 'tamb': np.mean})
df = pd.DataFrame.from_dict({k: v for k, v in list(nvalues.items()) if k != 'y3'})
first_name = request.args.get('firstname')
first_name = request.form.get('firstname')
s[:5] for s in buckets
the_list.sort
key=lambda item: (-len(item), item)
df = df.set_index(['TRX_DATE'])
list(accumulate(list(range(10))))
datetime.datetime.strptime('2013-1-25', '%Y-%m-%d').strftime('%m/%d/%y')
datetime.datetime.strptime('2013-1-25', '%Y-%m-%d').strftime('%-m/%d/%y')
df2 = df.ix
df.columns.str.endswith('prefix')
new_list = my_list[-10:]
my_list[-10:]
np.array(x._data).reshape(x.size[::-1]).T
df.groupby(level=0, as_index=False).nth(0)
numpy.concatenate(LIST, axis=0)
encode('utf-8').decode('unicode_escape')
encode('utf-8')
j for i in zip(a, b) for j in i
j for i in zip(a, b) for j in i
print([s.replace('8', '') for s in lst])
join('Hello')
Content.objects.all().order_by('?')[:100]
A[np.arange(A.shape[0])[:, (None)], B]
df.pivot_table(index='saleid', columns='upc', aggfunc='size', fill_value=0)
re.findall('([a-z]*)', 'f233op')
re.findall('([a-z])*', 'f233op')
re.split('_for_', 'happy_hats_for_cats')
re.split('_(?:for|or|and)_', 'sad_pandas_and_happy_cats_for_people')
re.split('_(?:f?or|and)_', s) for s in l
dict(zip(k, x)) for x in v
sorted(lst, reverse=True)
order_array.sort(order=['year', 'month', 'day'])
df.sort(['year', 'month', 'day'])
return my_list == list(range(my_list[0], my_list[-1] + 1))
df.groupby('id').agg(lambda x: x.tolist())
encode('raw_unicode_escape').decode('utf-8')
float(a)
getattr(a, 'property', 'default value')
np.delete(a, list(range(0, a.shape[1], 8)), axis=1)
datetime.datetime.fromtimestamp(ms / 1000.0)
np.einsum('...j,...j->...', vf, vf)
r = requests.get(url)
r = requests.get(url, params=payload)
r = requests.post(url, data=payload)
post_response = requests.post(url='http://httpbin.org/post', json=post_data)
mylist | slice
3
8
df1 = pd.read_hdf('/home/.../data.h5', 'firstSet')
max(test_string.rfind(i) for i in '([{')
print('here is your checkmark: ' + '\u2713')
print('\u0420\u043e\u0441\u0441\u0438\u044f')
print('{0}'.format('5'.zfill(2)))
sorted(set(itertools.chain.from_iterable(sequences)))
df['a'].values.tolist()
df['a'].tolist()
replace('""', '\\""')
print(all(word[0].isupper() for word in words))
myDict = {key: val for key, val in list(myDict.items()) if val != 42}
key: val
val in list(myDict.items()) 
val != 42
return len(s.encode('utf-8'))
os.kill(process.pid, signal.SIGKILL)
df[pd.isnull(df).any(axis=1)]
url.split('&')[-1].replace('=', '') + '.html'
parser.ParseFile(open('sample.xml', 'rb'))
sys.exit()
setattr(self, attr, group)
urllib.parse.unquote(urllib.parse.unquote(some_string))
urllib.parse.unquote(urllib.parse.unquote('FireShot3%2B%25282%2529.png'))
FireShot3%2
B%25282%2529.
FireShot3+(2).png
app.config['SECURITY_REGISTER_URL'] = '/create_account'
output = open('/home/user/test/wsservice/data.pkl', 'wb')
del a[(-1)
a.pop(1)
a.pop()
a.pop(index)
del a[index
ax.set_xlabel('Temperature (\u2103)')
ax.set_xlabel('Temperature ($^\\circ$C)')
join(l) for l in list_of_lists
pd.concat(g for _, g in df.groupby('ID') if len(g) > 1)
x = numpy.delete(x, 2, axis=1)
x = numpy.delete(x, 0, axis=0)
pd.concat((df1, df2), axis=1).mean(axis=1)
np.mean(np.array([old_set, new_set]), axis=0)
scatter(x, y, s=500, color='green', marker='h')
result = [item for word in words for item in word.split(',')]
datetime.datetime.strptime('2012-05-29T19:30:03.283Z', '%Y-%m-%dT%H:%M:%S.%fZ')
sum(item['one'] for item in list(tadas.values()))
a = open('pdf_reference.pdf', 'rb').read().encode('base64')
a.rstrip().split('\n')
a.split('\n')[:-1]
return HttpResponse(status=204)
7 in a
sorted(results, key=itemgetter('year'))
print(browser.current_url)
re.split('; |, ', str)
decode('unicode-escape')
time.mktime(datetime.datetime.strptime(s, '%d/%m/%Y').timetuple())
int(datetime.datetime.strptime('01/12/2011', '%d/%m/%Y').strftime('%s'))
request.headers['your-header-name']
df.groupby('User')['X'].filter(lambda x: x.sum() == 0)
df.loc[df.groupby('User')['X'].transform(sum) == 0]
df.groupby('User')['X'].transform(sum) == 0
df.set_index(['Name', 'Destination'])
print(re.sub('(\\W)\\1+', '\\1', a))
os.system('start ""$file""')
unicodedata.normalize('NFKD', title).encode('ascii', 'ignore')
a.encode('ascii', 'ignore')
files = [f for f in os.listdir('.') if re.match('[0-9]+.*\\.jpg', f)]
np.zeros((6, 9, 20)) + np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
None
None
np.zeros((6, 9, 20)) + np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape((1, 9, 1))
print(max(x, key=sum))
sum(len(y) for y in x if len(y) > 1)
re.sub('(\\d+)', '""\\1""', 'This is number 1 and this is number 22')
numpy.dot(numpy.dot(a, m), a)
Entry.objects.filter(name='name', title='title').exists()
l, key=lambda x: (-int(x[1]), x[0])
request.META['HTTP_HOST']
re.findall
api('randomkey123xyz987', 'key', 'text')
subprocess.call(['/usr/bin/perl', './uireplace.pl', var])
print('\n'.join(str(p) for p in myList))
mydic.update({i: o['name']})
list(stru.decode('utf-8'))
u = s.decode('utf-8-sig')
Entry.objects.filter
Q(id=3)
getattr(__builtins__, 'range')
subprocess.call(['shutdown', '/r', '/t', '900'])
subprocess.call(['shutdown', '/s'])
subprocess.call(['shutdown', '/a '])
subprocess.call(['shutdown', '/l '])
subprocess.call(['shutdown', '/r'])
open('filename', 'w').close()
df.to_dict('index')
df.to_dict('records')
df.groupby(pd.TimeGrouper(freq='M'))
c / t
t in zip(conversions, trials)
sorted(data, key=data.get)
sorted(data.values())
list(data.items())
key=lambda x: x[1]
now = datetime.datetime.now().strftime('%H:%M:%S')
replace('bar', 'XXX', 1).find('bar')
set(['stackoverflow', 'google']).issubset(sites)
stuff.replace(' and ', '/')
np.savez(tmp, *[getarray[0], getarray[1], getarray[8]])
t - datetime.timedelta(hours=1, minutes=10)
dt = datetime.datetime.combine(datetime.date.today(), t)
dt -= datetime.timedelta(hours=5)
print(data.encode('hex'))
print(' '.join([str(ord(a)) for a in data]))
x for x in l if x[1] == 1
a.fromlist([int(val) for val in stdin.read().split()])
print(re.sub('[_%^$]', '\\\\\\g<0>', line))
doc.xpath
a[starts-with(text(),'some text')]
zip(*a)
map(int, sublist) for sublist in lst
int(x) for x in sublist
sublist in lst
np.where(np.in1d(A, B))[0]
b in zip(d['key1'], d['key2'])
calendar.monthrange(2002, 1)
calendar.monthrange(2008, 2)
calendar.monthrange(2100, 2)
calendar.monthrange(year, month)[1]
monthrange(2012, 2)
datetime.date(2000, 2, 1) - datetime.timedelta(days=1)
from subprocess import call
os.system('some_command with args')
os.system('some_command < input_file | another_command > output_file')
stream = os.popen('some_command with args')
print(subprocess.Popen('echo Hello World', shell=True, stdout=subprocess.PIPE).stdout.read())
print(os.popen('echo Hello World').read())
return_code = subprocess.call('echo Hello World', shell=True)
call(['ls', '-l'])
print(urllib.parse.unquote(url).decode('utf8'))
url = urllib.parse.unquote(url).decode('utf8')
join(filter(str.isdigit, '12454v'))
df['Season'].str.split('-').str[0].astype(int)
my_list.sort
key=lambda x: x[1]
m.start() for m in re.finditer('(?=tt)', 'ttt')
m.start() for m in re.finditer('test', 'test test test test')
re.findall('\\s+|\\S+', s)
rdata.set_index(['race_date', 'track_code', 'race_number'])
list.sort
key=lambda item: item['date']
reverse=True
5
format('aaabbbccc')
struct.unpack('11B', s)
i for i, j in enumerate(['foo', 'bar', 'baz']) if j == 'foo'
print(list(itertools.product([1, 2, 3], [4, 5, 6])))
itertools.permutations([1, 2, 3])
return re.sub('\\p{P}+', '', text)
raise ValueError('A very specific bad thing happened')
raise Exception('I know Python!')
raise Exception('I know python!')
raise ValueError('represents a hidden bug, do not catch this')
raise Exception('This is the exception you expect to handle')
raise ValueError('A very specific bad thing happened')
raise RuntimeError('specific message')
raise AssertionError
driver.find_element_by_id('foo').clear()
driver.find_element_by_id('foo').clear()
socket.inet_ntoa(struct.pack('!L', 2130706433))
df = df[['x', 'y', 'a', 'b']]
super(ChildClass, self).__init__(*args, **kwargs)
sum(d.values())
json.dumps(your_data, ensure_ascii=False)
values = np.array([i for i in range(100)], dtype=np.float64)
list_of_dct, key=lambda x: order.index(list(x.values())[0])
return s[0].upper() + s[1:]
join([1, 2, 3, 4])
line = line.decode('utf-8', 'ignore').encode('utf-8')
os.system(command)
c.execute('SELECT * FROM foo WHERE bar = %s AND baz = %s', (param1, param2))
dateobj = datetime.datetime.strptime(datestr, '%Y-%m-%d').date()