# E120EAC

## Descrição

Vendas - Pedidos - Envio do Pedido para Análise de Crédito Externa

---

## Resumo

- Campos: 46
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqEac | Number(004,0) | Não | Sequência de envio do pedido para o autenticador externo |
| CodAec | Number(004,0) | Não | Código do autenticador externo de crédito de clientes |
| NroPro | Number(009,0) | Sim | Número da proposta na análise de crédito externa gerada pelo ERP |
| DatEmi | Date | Sim | Data de emissão do pedido |
| VlrTot | Number(015,2) | Sim | Valor total do pedido |
| VlrEnt | Number(015,2) | Sim | Valor da entrada do pedido |
| VlrFin | Number(015,2) | Sim | Valor financiado do pedido |
| TipEnt | String(020) | Sim | Tipo de entrega do pedido |
| ReaPed | String(001) | Sim | Reanálise do Pedido |
| TipNum | String(025) | Sim | Tipo de numerário do pedido (forma pagamento) |
| NomCli | String(100) | Não | Nome do cliente |
| ApeCli | String(050) | Não | Nome fantasia do cliente |
| CodCli | Number(009,0) | Não | Código do cliente |
| TipCli | String(001) | Não | Tipo do cliente |
| CodCca | String(003) | Sim | Código da categoria do cliente para a análise de crédito |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF do cliente |
| DocIde | String(014) | Sim | Número do CNPJ ou CPF do cliente |
| CodSex | String(003) | Sim | Código do sexo |
| EstCiv | Number(001,0) | Sim | Estado civil do cliente |
| DatNas | Date | Sim | Data do nascimento do cliente |
| CidNat | String(060) | Sim | Nome da cidade de naturalidade |
| CodPai | String(004) | Sim | Nome do país de nacionalidade do cliente |
| DesPai | String(150) | Não | Descrição País |
| NumRge | String(013) | Sim | Número do RG (Identidade) |
| DatRge | Date | Sim | Data de emissão do RG |
| OrgRge | String(006) | Sim | Órgão emissor do RG |
| NomMae | String(030) | Sim | Nome da mãe do cliente |
| NomPai | String(030) | Sim | Nome do pai do cliente |
| TipMor | Number(001,0) | Sim | Tipo de moradia do cliente |
| TpoMor | Date | Sim | Mês e ano da mudança para a moradia atual (reside desde) |
| NomSoc | String(030) | Sim | Nome do sócio |
| FonSoc | String(020) | Sim | Telefone Sócio |
| UsuExp | String(100) | Sim | Usuário na empresa externa |
| EmpExp | String(010) | Sim | Código da empresa na empresa externa |
| FilExp | Number(009,0) | Sim | Código da filial na empresa externa |
| SitEac | Number(001,0) | Sim | Situação Envio |
| TipAec | Number(001,0) | Sim | Tipo do autenticador externo de crédito de clientes |
| DesEac | String(2499) | Sim | Descrição retorno da consulta ao analisador externo |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| SeqEnv | Number(004,0) | Sim | Sequência do envio do pedido para todos os autenticadores |
| DatCon | Date | Sim | Data da consulta ao integrador externo |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqEac

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E120EAC_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

