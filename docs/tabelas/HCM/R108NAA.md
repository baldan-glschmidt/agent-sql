# R108NAA

## Descrição

Registro de Notificação Compulsória - Acidentes - Anexos

---

## Resumo

- Campos: 11
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAct | Date | Não | Data Acidente de Trabalho |
| HorAct | Number(005,0) | Não | Hora Acidente de Trabalho |
| DatCat | Date | Não | Data de registro da CAT |
| TipCat | Number(001,0) | Não | Tipo CAT |
| SeqArq | Number(003,0) | Não | Sequência do arquivo |
| NomArq | String(250) | Sim | Nome do arquivo de anexo |
| DesArq | String(060) | Sim | Descrição do anexo |
| ArqAne | Image | Sim | Anexo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAct
- HorAct
- DatCat
- TipCat
- SeqArq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
