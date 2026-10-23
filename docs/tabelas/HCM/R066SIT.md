# R066SIT

## Descrição

Situações Apuração Colaborador

---

## Resumo

- Campos: 13
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatApu | Date | Não | Data da Apuração |
| CodSit | Number(003,0) | Não | Código da Situação Apurada |
| CodRat | Number(009,0) | Não | Código de Rateio da Situação |
| QtdHor | Number(010,0) | Sim | Qtde de Horas Apuradas p/ a Situação |
| MotSit | Number(003,0) | Sim | Motivo da Situação |
| CodUsu | Number(010,0) | Sim | Código do Usuário do Último Acerto na Situação |
| QtdHNC | Number(010,0) | Sim | Qtde. Horas Situação s/Conversão de Noturnas |
| PerRef | Date | Sim | Competência do Cálculo |
| TipAgr | Number(002,0) | Sim | Tipo do agrupamento das situações |
| USU_RegImp | String(001) | Sim | Registro Importado p/ FPNG |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatApu
- CodSit
- CodRat

---

## Índices

### R066SITIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- PerRef

---

## Relacionamentos

### IR_R066SIT_004

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

