# R070LIJ

## Descrição

Autorização de Liberação de Interjonada

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatIni | Date | Não | Data Inicial da Liberação de Interjornada |
| HorIni | Number(005,0) | Não | Hora Inicial da Liberação de Interjornada |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador da Liberação de Interjornada |
| TclAut | Number(001,0) | Sim | Tipo de Colaborador do Autorizador da Liberação de Interjornada |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador da Liberação de Interjornada |
| ObsSij | String(080) | Sim | Observação da Liberação de Interjornada |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Liberação de Interjornada |
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTROLE (Acesso On-Line) |

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
