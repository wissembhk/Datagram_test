
from fastapi import APIRouter, FastAPI
from emailSender import send_mail
from consumer import Retrive_data_from_rabbit
from services.userService import create_db
from fastapi_utils.tasks import repeat_every
from routers import userRouter as userRouters

app = FastAPI()
create_db()
router = APIRouter(prefix="/api")

router.include_router(userRouters.router)
app.include_router(router)

# repeat the data retreiving task+sending the email with a report every 24hours


@app.on_event("startup")
@repeat_every(seconds=60*60*24)
async def rabbitmq_Data_Retriever():
    result = await Retrive_data_from_rabbit()
    send_mail(result)


# this endpoint was just implemented in case someone wants to try
# the mail sending without waiting the scheduled event
@app.post("/mailtesting")
async def send_mail_route():
    send_mail("this is just a test")
