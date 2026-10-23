# R058ACO

## Descrição

Modelo Acoplado

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ModRlg | Number(004,0) | Não | Código do Modelo do Coletor |
| ModAco | Number(004,0) | Não | Modelo Acoplado |
| SeqMod | Number(002,0) | Não | Sequência do Registro |
| ModEmb | String(001) | Sim | Modelo Embarcado |

---

## Chave Primária

- ModRlg
- ModAco
- SeqMod

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058ACO_000

**Tabela:** R058MOD

| Origem | Destino |
|--------|---------|
| ModRlg | ModRlg |

### IR_R058ACO_001

**Tabela:** R058MOD

| Origem | Destino |
|--------|---------|
| ModAco | ModRlg |

