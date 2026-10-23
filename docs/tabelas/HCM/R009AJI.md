# R009AJI

## Descrição

Gestão de Incidentes - Anexos das justificativas

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
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
| CodTAl | Number(002,0) | Não | Código do Incidentes |
| CodAji | Number(003,0) | Não | Código do Anexo da Justificativa |
| LobArq | Image | Sim | Arquivo Anexo |
| NomArq | String(050) | Sim | Nome do Arquivo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatApu
- CodTAl
- CodAji

---

## Índices

### R009AJIIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad

---

## Relacionamentos

Nenhum relacionamento cadastrado.
