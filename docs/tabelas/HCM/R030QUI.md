# R030QUI

## Descrição

Filiais da Empresa - Termos de Quitações

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| PerQui | Number(001,0) | Não | Período de Alteração |
| CmpAlt | Date | Não | Competência de Alteração |
| SeqQui | Number(009,0) | Não | Sequência da Quitação |
| DesQui | String(030) | Sim | Descrição da Quitação |
| DatDec | Date | Não | Data da Quitação |

---

## Chave Primária

- NumEmp
- CodFil
- PerQui
- CmpAlt
- SeqQui

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030QUI_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R030QUI_003

**Tabela:** R030TER

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| PerQui | PerQui |
| CmpAlt | CmpAlt |

