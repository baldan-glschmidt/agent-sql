# E070FTR

## Descrição

Cadastros - Filiais - Parâmetros Transporte

---

## Resumo

- Campos: 22
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| FreQmc | Number(002,0) | Sim | Quantidade mínima de cotações de frete |
| CodSer | String(014) | Sim | Código do serviço padrão para transportes |
| CodTpt | String(003) | Sim | Tipo de título gerado no contas a pagar pelo Manifesto |
| CgcRpt | String(001) | Sim | Indicativo se o CNPJ/CPF/Nº Identificação Fiscal da transportadora pode ser repetido |
| IntCte | String(001) | Sim | Forma de integração para conhecimento de transporte eletrônico |
| VisCte | String(001) | Sim | Indicativo se o CT-e será visualizada antes do envio |
| CmrCte | String(012) | Sim | Código do modelo do relatório para visualização do CT-e |
| CanEve | String(001) | Sim | [INUTILIZADO] Indicativo se utiliza o cancelamento como um evento do CT-e [INUTILIZADO] |
| NrnTrc | String(014) | Sim | Registro nacional de transportadores rodoviários de carga - RNTRC |
| CodOtm | String(020) | Sim | Código do operador multimodal |
| VenSct | String(003) | Sim | Série padrão de conhecimento de transporte. |
| PraCan | Number(003,0) | Sim | Prazo de cancelamento do CT-e em horas |
| VenSma | String(003) | Sim | Série padrão para Manifesto Eletrônico de Documentos |
| BltCte | String(001) | Sim | Indicativo se deve ser feita a geração automática de boletos do cupom eletrônico |
| CodSeg | Number(009,0) | Sim | Código da Seguradora |
| SctCos | String(003) | Sim | Série padrão de conhecimento de transporte outros serviços. |
| SrvCos | String(014) | Sim | Código do serviço padrão para conhecimento de transporte outros serviços. |
| CodTaf | String(012) | Sim | Termo de Autorização dos Serviços em Regime de Fretamento - TAF |
| NroRes | String(025) | Sim | Numero de registro adquirido junto a Administração Estadual. |
| CteGlo | String(001) | Sim | Indicativo se permite a emissão de CT-e Globalizado |

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
