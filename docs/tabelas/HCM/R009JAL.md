# R009JAL

## Descrição

Gestão de Incidentes - Justificar incidente

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
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
| CodTAl | Number(002,0) | Não | Código do Incidente |
| CodJip | Number(003,0) | Não | Código da justificativa de incidente |
| UsuGes | Number(010,0) | Não | Código do usuário |
| ObsGes | String(2000) | Sim | Observação gestor |
| DatUag | Date | Sim | Data última alteração gestor |
| UsuCol | Number(010,0) | Não | Código do usuário |
| ObsCol | String(2000) | Sim | Observação colaborador |
| DatCol | Date | Sim | Data última alteração colaborador |
| StaJal | Number(001,0) | Sim | Status do Incidente |
| PerRef | Date | Sim | Competência do Cálculo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatApu
- CodTAl

---

## Índices

### R009JALIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- PerRef

---

## Relacionamentos

Nenhum relacionamento cadastrado.
