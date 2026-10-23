# R066PEN

## Descrição

Pendências de acerto

---

## Resumo

- Campos: 13
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatApu | Date | Não | Data da Apuração |
| DatCri | Date | Sim | Data de criação |
| SitPen | Number(001,0) | Sim | Situação da pendência |
| UltMod | Date | Sim | Última modificação |
| UsuMod | String(255) | Sim | Usuário que modificou a pendência |
| NotCol | Number(001,0) | Sim | Notificação colaborador |
| ExpPen | Number(001,0) | Sim | Pendência expirou |
| DatExp | Date | Sim | Data que a pendência deve expirar |
| PRCIID | Number(010,0) | Sim | Identificador de instância do processo |
| PerRef | Date | Sim | Competência do Cálculo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatApu

---

## Índices

### R066PENIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- PerRef

---

## Relacionamentos

Nenhum relacionamento cadastrado.
