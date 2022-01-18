FROM python
RUN pip install flask
RUN pip install requests
COPY  ./static /home/devasc/CPE41S2/MidProjectG11/group11/static/
COPY  ./templates /home/devasc/CPE41S2/MidProjectG11/group11/templates/
COPY  main.py /home/devasc/CPE41S2/MidProjectG11/group11/
EXPOSE 8080
CMD python3 /home/devasc/CPE41S2/MidProjectG11/group11/main.py
