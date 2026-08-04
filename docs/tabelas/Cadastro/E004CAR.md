# E004CAR

## Descrição

Tabelas - Parâmetros - Carga

---

## Resumo

- Campos: 26
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| ObsCar | String(250) | Sim | Texto da observação |
| AbgPed | String(999) | Sim | Abrangência de pedidos |
| EntIni | Date | Sim | Data de entrega inicial para análise de embarque |
| EntFim | Date | Sim | Data de entrega final para análise de embarque |
| EmiIni | Date | Sim | Data de emissão de pedido inicial para análise de embarque |
| EmiFim | Date | Sim | Data de emissão de pedido final para análise de embarque |
| AbgTns | String(250) | Sim | Abrangência das transações dos pedidos |
| AbgCli | String(250) | Sim | Abrangência dos clientes dos pedidos |
| AbgCat | String(030) | Sim | Abrangência das categorias dos clientes dos pedidos |
| AbgRoe | String(250) | Sim | Abrangência das rotas de entrega dos clientes dos pedidos |
| AbgTra | String(250) | Sim | Abrangência das transportadoras/redespachos dos pedidos |
| CriCar | Number(001,0) | Não | Critério a ser adotado pela análise de embarque |
| CriSpd | Number(001,0) | Não | Critério de seleção dos pedidos para análise de embarque |
| CriEst | Number(001,0) | Não | Critério de cálculo dos estoques para efeito de análise |
| GerMvp | String(001) | Não | Indicativo se gera movimento de estoque pela pré-fatura |
| CriTre | Number(001,0) | Não | Critério de tratamento do estoque reservado para pedido não atendidos |
| GerPfb | String(001) | Não | Indicativo se gera pré-fatura com problema de crédito e cadastro (Bloqueada) |
| SitCar | Number(001,0) | Sim | Situação da Carga |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| CriGpf | Number(001,0) | Sim | Critério para geração de pré-faturas |
| QtdMpe | Number(014,5) | Sim | Quantidade mínima do pedido em estoque para gerar pré-fatura |
| PerMpe | Number(005,2) | Sim | Percentual mínimo do pedido em estoque para gerar pré-fatura |

---

## Chave Primária

- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
