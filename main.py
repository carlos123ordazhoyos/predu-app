from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from dotenv import load_dotenv
import os

# === Importaciones de configuración y módulos locales ===
from ml_models import (
    predecir_carrera_graphsage,
    predecir_facultad_psychological,
    model_graphsage,
    model_psychological,
)

# Correos (solo se llaman las funciones ya definidas en cada módulo)
from correos.enviar_codigo.email_send import enviar_email_codigo
from correos.enviar_reporte_academico.email_send import enviar_email_reporte_academico
from correos.enviar_reporte_psicologico.email_send import enviar_email_reporte_psicologico
from correos.enviar_resultados.email_send import enviar_email_resultado
from correos.enviar_bienvenida.email_send import enviar_email_bienvenida
from correos.enviar_subida_plan.email_send import enviar_email_subida_plan
from correos.enviar_validacion_tutor.email_send import enviar_email_validacion_tutor
from correos.enviar_validacion_academica_tutor.email_send import enviar_email_validacion_academica_tutor
from correos.enviar_validacion_psicologica_tutor.email_send import enviar_email_validacion_psicologica_tutor
from correos.enviar_actualizacion_perfil.email_send import enviar_email_actualizacion_perfil
from correos.enviar_union_institucion.email_send import enviar_email_union_institucion
from correos.enviar_retiro_institucion.email_send import enviar_email_retiro_institucion
from correos.enviar_bienvenida_tutor.email_send import enviar_email_bienvenida_tutor
from correos.enviar_estudiante_agregado_tutor.email_send import enviar_email_estudiante_agregado_tutor
from correos.enviar_tutor_agregado_grupo.email_send import enviar_email_tutor_agregado_grupo
from correos.tutor_cuenta_aprobada.email_send import enviar_email_tutor_cuenta_aprobada
from correos.tutor_cuenta_rechazada.email_send import enviar_email_tutor_cuenta_rechazada
from correos.cuenta_pago_finalizado.email_send import enviar_email_pago_finalizado


# === 1. Cargar entorno ===
load_dotenv()

# === 2. Inicializar app ===
app = FastAPI(
    title="PREDU Vocacional API",
    description="API para predicción vocacional, envío de reportes y códigos de acceso.",
    version="2.0.0"
)

# === 3. Configurar CORS ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === 4. Modelos Pydantic ===
class EstudianteInput(BaseModel):
    arte_y_cultura: str
    castellano_como_segunda_lengua: str
    ciencia_y_tecnologia: str
    ciencias_sociales: str
    comunicacion: str
    desarrollo_personal: str
    educacion_fisica: str
    educacion_para_el_trabajo: str
    educacion_religiosa: str
    ingles: str
    matematica: str


class PsicoInput(BaseModel):
    realista: float
    investigador: float
    artistico: float
    social: float
    emprendedor: float
    convencional: float


class CodigoAccesoEmail(BaseModel):
    email: EmailStr
    nombre_estudiante: str
    institucion: str
    region: str
    unique_code: str
    director_name: str
    teaching_modality: str


class ReporteAcademicoEmail(BaseModel):
    email: EmailStr
    nombre_estudiante: str
    facultad_academica: str
    recomendacion_academica: str


class ReportePsicologicoEmail(BaseModel):
    email: EmailStr
    nombre_estudiante: str
    facultad_psicologica: str
    consejo_psicologico: str


class ReporteResultadoEmail(BaseModel):
    email: EmailStr
    nombre_estudiante: str
    facultad_academica: str
    facultad_psicologica: str

class BienvenidaEmail(BaseModel):
    email: EmailStr
    nombre_estudiante: str

class SubidaPlanEmail(BaseModel):
    email: EmailStr
    nombre_estudiante: str
    nuevo_plan: str

class ValidacionTutorEmail(BaseModel):
    email: EmailStr
    nombre_estudiante: str
    nombre_tutor: str
    consejo_tutor: str

class ValidacionAcademicaTutorEmail(BaseModel):
    email: EmailStr
    nombre_estudiante: str
    nombre_tutor: str
    consejo_tutor: str

class ValidacionPsicologicaTutorEmail(BaseModel):
    email: EmailStr
    nombre_estudiante: str
    nombre_tutor: str
    consejo_tutor: str

class ActualizacionPerfilEmail(BaseModel):
    email: EmailStr
    nombre_estudiante: str
    cambios_realizados: list[str]

class UnionInstitucionEmail(BaseModel):
    email: EmailStr
    nombre_estudiante: str
    nombre_institucion: str
    lugar: str
    nombre_encargado: str
    logo_url: str
    mensaje_motivador: str

class RetiroInstitucionEmail(BaseModel):
    email: EmailStr
    nombre_estudiante: str
    nombre_institucion: str
    lugar: str
    nombre_encargado: str
    motivo_retiro: str
    logo_url: str

class BienvenidaTutorEmail(BaseModel):
    email: EmailStr
    nombre_tutor: str
    institucion: str
    logo_url: str
    enlace_panel: str

class EstudianteAgregadoTutorEmail(BaseModel):
    email_tutor: EmailStr
    nombre_tutor: str
    nombre_estudiante: str
    grado: str
    correo: str
    telefono: str
    logo_url: str

class TutorAgregadoGrupoEmail(BaseModel):
    email_destino: EmailStr
    nombre_grupo: str
    nombre_tutor: str
    tipo_tutor: str
    correo: str
    telefono: str
    logo_url: str

class TutorCuentaAprobadaEmail(BaseModel):
    email: EmailStr
    nombre_tutor: str
    fecha_aprobacion: str
    logo_url: str

class TutorCuentaRechazadaEmail(BaseModel):
    email: EmailStr
    nombre_tutor: str
    motivo_rechazo: str
    fecha_revision: str
    logo_url: str

class PagoFinalizadoEmail(BaseModel):
    email: EmailStr
    nombre_estudiante: str
    tipo_cuenta: str
    fecha_fin: str
    logo_url: str

# === 5. Endpoints de predicción ===

@app.post("/prediccion/academico/")
async def prediccion_academica(data: EstudianteInput):
    """Predice la facultad sugerida según el rendimiento académico."""
    new_student_data = [
        data.arte_y_cultura,
        data.castellano_como_segunda_lengua,
        data.ciencia_y_tecnologia,
        data.ciencias_sociales,
        data.comunicacion,
        data.desarrollo_personal,
        data.educacion_fisica,
        data.educacion_para_el_trabajo,
        data.educacion_religiosa,
        data.ingles,
        data.matematica
    ]
    facultad_academica = predecir_carrera_graphsage(model_graphsage, new_student_data)
    return {"facultad_academica": facultad_academica}


@app.post("/prediccion/psicologica/")
async def prediccion_psicologica(data: PsicoInput):
    """Predice la facultad sugerida según el perfil psicológico (modelo RIASEC)."""
    new_student_psychological = [
        data.realista,
        data.investigador,
        data.artistico,
        data.social,
        data.emprendedor,
        data.convencional
    ]
    facultad_psicologica = predecir_facultad_psychological(model_psychological, new_student_psychological)
    return {"facultad_psicologica": facultad_psicologica}


# === 6. Endpoints de envío de correos (modularizados) ===

@app.post("/enviar-codigo/")
async def enviar_codigo(data: CodigoAccesoEmail, background_tasks: BackgroundTasks):
    return await enviar_email_codigo(data, background_tasks)


@app.post("/enviar-reporte-academico/")
async def enviar_reporte_academico(data: ReporteAcademicoEmail, background_tasks: BackgroundTasks):
    return await enviar_email_reporte_academico(data, background_tasks)


@app.post("/enviar-reporte-psicologico/")
async def enviar_reporte_psicologico(data: ReportePsicologicoEmail, background_tasks: BackgroundTasks):
    return await enviar_email_reporte_psicologico(data, background_tasks)


@app.post("/enviar-reporte-resultado/")
async def enviar_reporte_resultado(data: ReporteResultadoEmail, background_tasks: BackgroundTasks):
    return await enviar_email_resultado(data, background_tasks)

@app.post("/enviar-bienvenida/")
async def enviar_bienvenida(data: BienvenidaEmail, background_tasks: BackgroundTasks):
    return await enviar_email_bienvenida(data, background_tasks)

@app.post("/enviar-subida-plan/")
async def enviar_subida_plan(data: SubidaPlanEmail, background_tasks: BackgroundTasks):
    return await enviar_email_subida_plan(data, background_tasks)

@app.post("/enviar-validacion-tutor/")
async def enviar_validacion_tutor(data: ValidacionTutorEmail, background_tasks: BackgroundTasks):
    return await enviar_email_validacion_tutor(data, background_tasks)

@app.post("/enviar-validacion-academica-tutor/")
async def enviar_validacion_academica_tutor(data: ValidacionAcademicaTutorEmail, background_tasks: BackgroundTasks):
    return await enviar_email_validacion_academica_tutor(data, background_tasks)

@app.post("/enviar-validacion-psicologica-tutor/")
async def enviar_validacion_psicologica_tutor(data: ValidacionPsicologicaTutorEmail, background_tasks: BackgroundTasks):
    return await enviar_email_validacion_psicologica_tutor(data, background_tasks)

@app.post("/enviar-actualizacion-perfil/")
async def enviar_actualizacion_perfil(data: ActualizacionPerfilEmail, background_tasks: BackgroundTasks):
    return await enviar_email_actualizacion_perfil(data, background_tasks)

@app.post("/enviar-union-institucion/")
async def enviar_union_institucion(data: UnionInstitucionEmail, background_tasks: BackgroundTasks):
    return await enviar_email_union_institucion(data, background_tasks)

@app.post("/enviar-retiro-institucion/")
async def enviar_retiro_institucion(data: RetiroInstitucionEmail, background_tasks: BackgroundTasks):
    return await enviar_email_retiro_institucion(data, background_tasks)

@app.post("/enviar-bienvenida-tutor/")
async def enviar_bienvenida_tutor(data: BienvenidaTutorEmail, background_tasks: BackgroundTasks):
    return await enviar_email_bienvenida_tutor(data, background_tasks)

@app.post("/enviar-estudiante-agregado-tutor/")
async def enviar_estudiante_agregado_tutor(data: EstudianteAgregadoTutorEmail, background_tasks: BackgroundTasks):
    return await enviar_email_estudiante_agregado_tutor(data, background_tasks)

@app.post("/enviar-tutor-agregado-grupo/")
async def enviar_tutor_agregado_grupo(data: TutorAgregadoGrupoEmail, background_tasks: BackgroundTasks):
    return await enviar_email_tutor_agregado_grupo(data, background_tasks)

@app.post("/enviar-tutor-cuenta-aprobada/")
async def enviar_tutor_cuenta_aprobada(data: TutorCuentaAprobadaEmail, background_tasks: BackgroundTasks):
    return await enviar_email_tutor_cuenta_aprobada(data, background_tasks)

@app.post("/enviar-tutor-cuenta-rechazada/")
async def enviar_tutor_cuenta_rechazada(data: TutorCuentaRechazadaEmail, background_tasks: BackgroundTasks):
    return await enviar_email_tutor_cuenta_rechazada(data, background_tasks)

@app.post("/enviar-pago-finalizado/")
async def enviar_pago_finalizado(data: PagoFinalizadoEmail, background_tasks: BackgroundTasks):
    return await enviar_email_pago_finalizado(data, background_tasks)


# === 7. Ejecución del servidor ===
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
