# E070FPR

## Descrição

Cadastros - Filiais - Parâmetros para Manufatura e Serviços

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| TnsRnc | String(005) | Sim | Transação de estoque para entrada de reaproveitamento de material não conforme |
| RepMov | String(001) | Sim | Indicativo se as OPs de reprocesso movimentam estoque |
| RepTep | String(005) | Sim | Transação padrão para entrada no estoque em OPs de Reprocesso |
| RepTsp | String(005) | Sim | Transação padrão para saída do estoque em OPs de Reprocesso |
| CcuApr | Number(001,0) | Sim | Centro de custos que é sugerido via tela de apontamento de produção. |

---

## Chave Primária

- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E070FPR_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

