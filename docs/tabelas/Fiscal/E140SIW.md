# E140SIW

## Descrição

Integração WMS - Nota Fiscal de Saída - Situação da integração com WMS

---

## Resumo

- Campos: 21
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| Ideuni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| EstWms | Number(002,0) | Sim | Código do estágio no WMS |
| ReaPed | String(001) | Sim | Indicativo se reabilita o pedido |
| ReaPfa | String(001) | Sim | Indicativo se reabilita pré-fatura |
| SitOpc | Number(002,0) | Sim | Situação atual da operação de cancelamento ou devolução |
| TipOpe | Number(001,0) | Sim | Tipo da operação a executar sobre a nota fiscal de saída |
| CodMot | Number(006,0) | Sim | Código do motivo do cancelamento ou devolução |
| ObsMot | String(500) | Sim | Observação do motivo do cancelamento ou devolução |
| ObsSit | String(500) | Sim | Observação da situação do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| IdeOsc | String(050) | Sim | Identificador da Ordem de Separação - Dados Gerais |
| PedCli | String(020) | Sim | Número do pedido do cliente |
| CodFor | Number(009,0) | Sim | Código do fornecedor da nota fiscal de entrada, quando gerado devolução |
| NumNfc | Number(009,0) | Sim | Número da nota fiscal de entrada |
| SnfNfc | String(003) | Sim | Código da série da nota fiscal de entrada, quando gerada devolucao |

---

## Chave Primária

- Ideuni

---

## Índices

### E140SIWIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodSnf
- NumNfv

### E140SIWIndice2

**Tipo:** Não unico

Campos:
- IdeOsc

---

## Relacionamentos

### IR_E140SIW_004

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

