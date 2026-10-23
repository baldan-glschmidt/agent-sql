# R030PRH

## Descrição

Processos Judiciais - Histórico Alterações

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodPro | Number(009,0) | Não | Número do Processo/Benefício |
| DatIni | Date | Não | Data de Alteração |
| DatEnc | Date | Sim | Data de Encerramento do Processo |
| IndVar | String(004) | Sim | Identificação da Vara |
| EstVar | String(002) | Sim | Unidade Federativa da Vara |
| CidPro | Number(007,0) | Sim | Cidade |
| AutPro | Number(001,0) | Sim | Autoria |
| ObsAlt | String(255) | Sim | Observação |
| MatPro | Number(002,0) | Sim | Indicativo de matéria do processo ou alvará judicial |

---

## Chave Primária

- NumEmp
- CodPro
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
