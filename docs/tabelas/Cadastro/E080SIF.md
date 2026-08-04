# E080SIF

## Descrição

Tabelas - Serviços - Serviços intermediados X Filiais

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeCsi | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SitReg | String(001) | Sim | Situação do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeCsi
- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E080SIF_000

**Tabela:** E080CSI

| Origem | Destino |
|--------|---------|
| IdeCsi | IdeUni |

