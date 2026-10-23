# R030DIG

## Descrição

Filiais da Empresa - Assinatura Digitalizada

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa do colaborador |
| CodFil | Number(006,0) | Não | Código da Filial |
| AssDig | Image | Sim | Assinatura Digitalizada |

---

## Chave Primária

- NumEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030DIG_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

