# E070OPN

## Descrição

Tabelas - Integrações - Operações de nota fiscal do sistema a integrar

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodInt | Number(002,0) | Não | Código do sistema integrado |
| CodOpn | Number(004,0) | Sim | Código da operação de nota fiscal para integração entre sistemas. |
| EntSai | String(001) | Não | Indicativo se é nota fiscal de entrada ou saída |
| DesOpn | String(050) | Não | Descrição da Operação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E000OPNIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodInt
- CodOpn

---

## Relacionamentos

Nenhum relacionamento cadastrado.
