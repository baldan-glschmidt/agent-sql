# R070SIJ

## Descrição

Solicitação de Liberação de Interjornada

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa para Liberação de Interjornada |
| TipCol | Number(001,0) | Não | Tipo Colaborador para Liberação de Interjornada |
| NumCad | Number(009,0) | Não | Cadastro Colaborador para Liberação de Interjornada |
| DatIni | Date | Não | Data Inicial da Liberação de Interjornada |
| HorIni | Number(005,0) | Não | Hora Inicial da Liberação de Interjornada |
| EmpSol | Number(004,0) | Sim | Código da Empresa do Solicitante |
| TclSol | Number(001,0) | Sim | Tipo de Colaborador que Solicitou a Liberação de Interjornada |
| CadSol | Number(009,0) | Sim | Cadastro do Solicitante |
| ObsSij | String(080) | Sim | Observação da Liberação de Interjornada |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Liberação de Interjornada |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
