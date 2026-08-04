# E051RNF

## Descrição

Tabelas - Impostos - Dispositivos Fiscais - Reinf

---

## Resumo

- Campos: 16
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodDfs | Number(006,0) | Não | Código do dispositivo fiscal |
| TipAdv | String(001) | Sim | Tipo de Inscrição do Advogado |
| DocAdv | Number(014,0) | Sim | CNPJ ou CPF do Advogado |
| DocIdeAdv | String(014) | Sim | CNPJ ou CPF do Advogado |
| NomAdv | String(150) | Sim | Nome do advogado ou escritório de advocacia |
| VlrAdv | Number(015,2) | Sim | Valor da Despesa com o Advogado |
| DatLau | Date | Sim | Data atribuída pelo laudo da moléstia grave |
| IndRra | Number(001,0) | Não | Identificador de rendimento recebido acumuladamente |
| NatRra | String(050) | Sim | Natureza do RRA |
| IndOre | Number(001,0) | Sim | Indicativo de origem do recurso |
| CnpOri | Number(014,0) | Sim | CNPJ da Empresa que Repassou Recursos |
| DocIdeOri | String(014) | Sim | CNPJ da Empresa que Repassou Recursos |
| VlrDep | Number(015,2) | Sim | Valor das despesas com custas judiciais |
| QtdMes | Number(005,1) | Sim | Numero de meses relativo aos rendimentos recebidos acumuladamente |
| CpfOri | Number(011,0) | Sim | CPF da pessoa fisica que repassou recursos |

---

## Chave Primária

- CodEmp
- CodDfs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
