# R030PPP

## Descrição

Filiais da Empresa - Assinatura Dig. Responsável PPP

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
| AssPPP | Image | Sim | Assinatura Digitalizada do Responsável pelo PPP |

---

## Chave Primária

- NumEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030PPP_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

