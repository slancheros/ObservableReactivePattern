from rx import Observable

# Contextlib documentation https://docs.python.org/3/library/contextlib.html
# SringIO  https://docs.python.org/2/library/stringio.html

def get_quotes():
    import contextlib,io
    zen =io.StringIO()
    with contextlib.redirect_stdout(zen):
        import this

    quotes=zen.getvalue().split('\n')[1:]
    return enumerate(quotes)

zen_quotes = get_quotes()

Observable.interval(5000) \
    .flat_map(lambda seg: Observable.from_(zen_quotes)) \
    .flat_map(lambda q: Observable.from_(q[1].split())) \
    .filter(lambda s: len(s)>2) \
    .map( lambda s: s.replace('.','').replace(',','').replace('!','').replace('-','') ) \
    .map( lambda s: s.lower()) \
    .subscribe(lambda value: print(f"Received: {value}"))
  #  .flat_map(lambda q: Observable.from_(q[1].split())) \
  #  .filter(lambda s: len(s)>2) \
  # .map( lambda s: s.replace('.','').replace(',','').replace('!','').replace('-','') ) \
  # .map( lambda s: s.lower()) \


input("Starting... Press any key to quit\n")