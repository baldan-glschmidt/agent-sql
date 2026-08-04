# E068UST

## Descrição

Tabelas - Usuários de Substituição da Aprovação Multinível

---

## Resumo

- Campos: 15
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| RotNap | Number(002,0) | Não | Código da rotina para controle de níveis de aprovação |
| CodUsu | Number(010,0) | Não | Usuário pertencente a rotina de aprovação que será substituído |
| DatIni | Date | Não | Data de Início da Substituição |
| UsuSub | Number(010,0) | Não | Usuário subsittuto na aprovação multinível |
| DatIns | Date | Não | Data de Início da Substituição |
| DatFis | Date | Sim | Data de Fim da Substituição |
| SitSub | String(001) | Não | Situação do registro de substituição |
| ObsSub | String(250) | Sim | Observação da Substituição |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- RotNap
- CodUsu
- DatIni
- UsuSub
- DatIns

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
