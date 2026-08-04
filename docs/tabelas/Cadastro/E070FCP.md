# E070FCP

## Descrição

Cadastros - Filiais - Parâmetros Contas a Pagar

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| TnsEcs | String(005) | Sim | Transação padrão de entrada de títulos de contrato de aplicação/captação de recursos por substituição |
| TnsBto | String(005) | Sim | Transação para baixa dos títulos do contrato original em cotratos derivativos swap |
| PadTpt | String(003) | Sim | Tipo de título padrão para pagamento de ajuste em contrato derivativo |
| PadTns | String(005) | Sim | Transação padrão para pagamento de ajuste em contrato derivativo |

---

## Chave Primária

- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E070FCP_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

