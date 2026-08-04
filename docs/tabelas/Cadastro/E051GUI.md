# E051GUI

## Descrição

Tabelas - Impostos - Guias de Recolhimento

---

## Resumo

- Campos: 19
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodGri | Number(004,0) | Não | Código da guia de recolhimento |
| DesGui | String(030) | Não | Descrição da guia de recolhimento |
| AbrGui | String(003) | Sim | Abreviatura de guia de recolhimento |
| SigUfs | String(002) | Não | Sigla do estado favorecido |
| CodFis | Number(006,0) | Não | Código fiscal para a guia de recolhimento |
| CodDrf | Number(006,0) | Sim | Código para documento de arrecadação |
| InfEle | String(001) | Sim | Informado em arquivos eletrônicos fiscais |
| CodMdr | String(012) | Sim | Código do modelo para impressão da guia de recolhimento |
| SitGui | String(001) | Sim | Situação da guia de recolhimento |
| OriPgt | Number(001,0) | Sim | Origem da discriminação dos pagamentos de impostos |
| ClaVen | Number(005,0) | Sim | Código de Identificação de Débito |
| TipGui | Number(002,0) | Sim | Tipo da guia de recolhimento |
| DetRec | Number(006,0) | Sim | Código de detalhamento da receita |
| GruTri | Number(002,0) | Sim | Grupo de Tributos Utilizado na Declaração DCTF |
| DetPro | String(001) | Sim | Detalhamento por produto da GNRE |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
| ConMer | String(030) | Sim | Número do convênio ou protocolo / especificação da mercadoria |
| TdcOri | Number(002,0) | Sim | Tipo de documento origem GNRE |

---

## Chave Primária

- CodEmp
- CodGri

---

## Índices

### E051GUIIndice2

**Tipo:** Não unico

Campos:
- SigUfs
- CodFis

---

## Relacionamentos

Nenhum relacionamento cadastrado.
