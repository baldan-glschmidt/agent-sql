# R034PRM_AUD

## Descrição

Auditoria Permissão de Acesso por Colaborador

---

## Resumo

- Campos: 12
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(015,0) | Não | Sequencia do Registro |
| VerSeq | Number(010,0) | Não | Versão da Sequencia |
| IdtPes | String(023) | Não | Identificador da Pessoa |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor |
| VerPlf | Number(003,0) | Não | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Não | Código do Local Físico |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| NumAmb | Number(009,0) | Sim | Ambiente da Planta |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |

---

## Chave Primária

- SeqReg
- VerSeq
- IdtPes
- CodPlt
- CodRlg
- VerPlf
- CodPlf
- CodDsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
