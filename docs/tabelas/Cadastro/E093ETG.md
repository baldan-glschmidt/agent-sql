# E093ETG

## Descrição

Tabelas - Estágios da Produção

---

## Resumo

- Campos: 21
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodEtg | Number(004,0) | Não | Código do Estágio Produção (Etapas na Fabricação de um Produto) |
| DesEtg | String(030) | Não | Descrição do Estágio de Produção |
| AbrEtg | String(010) | Não | Abreviatura do Estágio de Produção |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |
| CodCcu | String(009) | Não | Código do Centro de Custo onde está agregado o Estágio. |
| CodOri | String(003) | Sim | Código de Origem do Produto que o Estágio fabrica |
| TipEtg | String(001) | Não | Tipo de Estágio (I=Interno, E=Externo) |
| UtiCel | String(001) | Não | Indica se Estágio é Administrado por Células de Produção |
| PtoIql | String(001) | Não | Indica se Estágio é Ponto de Inspeção de Qualidade |
| MovAut | String(001) | Não | Indica se Movimenta Início do Estágio Automaticamente Após Fim do Anterior |
| CqtPaf | String(001) | Não | Colocar estágio atual automaticamente em andamento mesmo com quantidade inferior a prevista? |
| CodLoc | String(024) | Sim | Código do Local conforme Organograma da Empresa (Sistema Vetorh) |
| MovGop | String(001) | Não | Movimentação da Produção é realizada c/ Guias de Produção da O.P. |
| QtdGop | Number(012,5) | Sim | Quantidade máxima para cada guia de produção do Estágio |
| AtuOpr | String(001) | Sim | Atualiza Operador na Baixa dos Componentes deste Estágio |
| IndSer | String(001) | Sim | Indicativo de uso exlusivo para modelo de OS |
| IdeUG7 | Number(010,0) | Sim | Identificador único do estágio da G7, para manter referência com a plataforma G7 |

---

## Chave Primária

- CodEmp
- CodEtg

---

## Índices

### E093ETGIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodCcu

---

## Relacionamentos

### IR_E093ETG_008

**Tabela:** E044CCU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCcu | CodCcu |

