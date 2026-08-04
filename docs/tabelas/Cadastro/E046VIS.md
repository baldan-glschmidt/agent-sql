# E046VIS

## Descrição

Tabelas - Visões Contábeis - Visão

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
| CodVis | String(020) | Não | Código da visão |
| DesVis | String(060) | Sim | Descrição da visão |
| ClaCta | String(025) | Sim | Classificação da visão |
| TipVis | String(001) | Sim | Indicativo de tipo de visão contábil |
| TipDco | Number(001,0) | Sim | Indica o tipo da demonstração contábil a qual a visão representa |
| QtdCol | Number(002,0) | Sim | Quantidade de colunas disponibilizadas na visão |
| PerVis | String(001) | Sim | Periodicidade para carga da visão |
| DesZer | String(001) | Sim | Indicativo que a busca dos valores irá desconsiderar o zeramento contábil |
| SitVis | String(001) | Sim | Situação da visão |
| ObsVis | String(1999) | Sim | Observações da visão |
| VisSis | String(001) | Sim | Indicativo que a visão é de propriedade do sistema |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| OrdPro | String(001) | Sim | indicativo que o campo NU_ORDEM será gerado pela ordem que as contas foram montadas na visão, ou se pegará o valor do campo E046PLA.OrdSpd |

---

## Chave Primária

- CodEmp
- CodVis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
