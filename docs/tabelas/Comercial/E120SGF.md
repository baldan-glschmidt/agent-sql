# E120SGF

## Descrição

Vendas - Pedidos - Controle das sugestões de frete recebidas da simulação

---

## Resumo

- Campos: 22
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqSml | Number(009,0) | Não | Sequência da simulação de frete |
| SeqSgf | Number(009,0) | Não | Sequência da sugestão de frete |
| CgcCpf | String(020) | Sim | CNPJ/CPF da transportadora |
| NomTra | String(100) | Sim | Nome da transportadora |
| ApeTra | String(050) | Sim | Nome fantasia da transportadora |
| CepTra | Number(008,0) | Sim | CEP da transportadora |
| EndTra | String(100) | Sim | Endereço da transportadora |
| NenTra | String(060) | Sim | Número da transportadora |
| CplEnd | String(200) | Sim | Complemento do endereço da transportadora |
| BaiTra | String(075) | Sim | Bairro da transportadora |
| CidTra | String(060) | Sim | Cidade da transportadora |
| SigUfs | String(002) | Sim | Estado do endereço da transportadora |
| VlrTot | Number(015,2) | Sim | Valor total do frete |
| VlrCtb | Number(015,2) | Sim | Valor contábil do frete |
| VlrPag | Number(015,2) | Sim | Valor do frete a pagar |
| DesPrz | String(100) | Sim | Descrição do prazo de entrega |
| UsuApr | Number(010,0) | Sim | Usuário responsável pela aprovação |
| DatApr | Date | Sim | Data da aprovação |
| HorApr | Number(005,0) | Sim | Hora da aprovação |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqSml
- SeqSgf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
