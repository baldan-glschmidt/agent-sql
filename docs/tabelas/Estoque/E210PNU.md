# E210PNU

## Descrição

Estoques - Produtos Numerados

---

## Resumo

- Campos: 17
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto em estoque |
| CodDer | String(007) | Não | Código da derivação do produto em estoque |
| CodDep | String(010) | Não | Código do depósito |
| NumSep | String(050) | Não | Número de série do produto |
| NumDoc | Number(009,0) | Sim | Número de documento base da numeração |
| FilPed | Number(005,0) | Sim | Código da filial do pedido |
| NumPed | Number(008,0) | Sim | Número do pedido que gerou o número de série |
| SeqIpd | Number(004,0) | Sim | Sequência do item no pedido |
| SitPnu | Number(001,0) | Não | Situação do registro de numeração |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| ObsPnu | String(250) | Sim | Observação |
| DatNum | Date | Sim | Data da confirmação da numeração da série |
| OriOrp | String(003) | Sim | Código da Origem de Produto da OP (Quando Movimento é de uma OP específica) |
| UsuLei | Number(010,0) | Sim | Usuário responsável pela leitura do registro |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodDep
- NumSep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
