# R030TER

## Descrição

Filiais da Empresa - Termo Quitação

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| PerQui | Number(001,0) | Não | Período de Alteração |
| CmpAlt | Date | Não | Competência de Alteração |
| ObsAlt | String(255) | Sim | Observação |

---

## Chave Primária

- NumEmp
- CodFil
- PerQui
- CmpAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030TER_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

