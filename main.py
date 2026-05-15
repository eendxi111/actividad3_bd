import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Date, insert
from sqlalchemy.orm import declarative_base
from faker import Faker


def main():

    # Cargar variables
    load_dotenv()

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")


    engine = create_engine(
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
    )


    try:

        with engine.connect() as conn:

            print("✅ Conexión exitosa")

            Base = declarative_base()


            class Persona(Base):

                __tablename__ = "personas_eendxi"


                id = Column(Integer,
                            primary_key=True,
                            autoincrement=True)

                nombre = Column(String(50))
                apellido = Column(String(50))
                telefono = Column(String(30))
                email = Column(String(100))
                ciudad = Column(String(100))
                direccion = Column(String(200))
                empresa = Column(String(100))
                fecha_nacimiento = Column(Date)


            Base.metadata.create_all(engine)

            print("✅ Tabla creada")


            fake = Faker("es_ES")


            data = []


            for _ in range(100000):

                data.append({

                    "nombre":
                    fake.first_name(),

                    "apellido":
                    fake.last_name(),

                    "telefono":
                    fake.phone_number(),

                    "email":
                    fake.email(),

                    "ciudad":
                    fake.city(),

                    "direccion":
                    fake.address(),

                    "empresa":
                    fake.company(),

                    "fecha_nacimiento":
                    fake.date_of_birth(
                        minimum_age=18,
                        maximum_age=90
                    )

                })


            print("✅ Datos generados")


            conn.execute(
                insert(Persona),
                data
            )


            conn.commit()


            print(
                "✅ 100000 registros insertados"
            )


    except Exception as e:

        print("❌ Error:", e)



if __name__ == "__main__":

    main()