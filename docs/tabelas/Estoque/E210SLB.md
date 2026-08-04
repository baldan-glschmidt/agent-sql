# E210SLB

## Descrição

Estoques - Saldos da Limpeza de Base

---

## Resumo

- Campos: 20
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| FilDep | Number(005,0) | Não | Código da filial que o depósito pertence |
| CodPro | String(014) | Não | Código do produto em estoque |
| CodDer | String(007) | Não | Código da derivação do produto em estoque |
| CodDep | String(010) | Não | Código do depósito |
| CodLot | String(050) | Não | Código do Lote de Fabricação para estocagem |
| QtdEst | Number(014,5) | Sim | Quantidade física total do estoque no depósito na data da limpeza de base |
| VlrEst | Number(015,2) | Sim | Valor em estoque total na data da limpeza de base |
| QtdBlo | Number(014,5) | Sim | Quantidade de estoque bloqueado na data da limpeza de base |
| QtdRes | Number(014,5) | Sim | Quantidade do estoque reservado na data da limpeza de base |
| QtdCfo | Number(014,5) | Sim | Quantidade consignada de fornecedores na data da limpeza de base |
| QtdCcl | Number(014,5) | Sim | Quantidade consignada para clientes  na data da limpeza de base |
| PrmEst | Number(021,10) | Sim | Preço Médio do estoque na data da limpeza de base |
| DatLbd | Date | Sim | Data da limpeza de base |
| DatGer | Date | Sim | Data da geração da Limpeza de Base |
| HorGer | Number(005,0) | Sim | Hora da geração da Limpeza de base |
| UsuGer | Number(010,0) | Sim | Número do cadastro do usuário que executou a limpeza de base |
| VlrIcm | Number(015,2) | Sim | Valor de ICMS |
| PrmIcm | Number(015,6) | Sim | Preço Médio do valor total de ICMS |
| IcmAcf | Number(015,2) | Sim | Valor total de ICMS acumulado para a filial |

---

## Chave Primária

- CodEmp
- FilDep
- CodPro
- CodDer
- CodDep
- CodLot

---

## Índices

### E210SLBIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro
- CodDer
- CodDep

---

## Relacionamentos

### IR_E210SLB_004

**Tabela:** E210EST

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |
| CodDep | CodDep |

