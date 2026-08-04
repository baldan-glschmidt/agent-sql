# E725CRE

## Descrição

Ficha - Roteiro - Cadastro Centro de Recursos

---

## Resumo

- Campos: 38
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodCre | String(008) | Não | Código do Centro de Recurso (conjunto Máquina/Pessoa c/ mesma capacidade produtiva) |
| DesCre | String(040) | Não | Descrição do Centro de Recurso |
| AbrCre | String(010) | Não | Abreviatura do Centro de Recursos |
| CodEtg | Number(004,0) | Sim | Estágio Produção |
| TipCre | String(001) | Não | Tipo C. Recursos (I=Interno - da própria fábrica, E=Terceiros - Externo) |
| LimCap | String(001) | Não | Limitação Capacidade (M=Máquinas, P=Pessoas, I=Ilimitada) |
| QtdMaq | Number(008,2) | Sim | Quantidade de Máquinas (equipamentos diversos) |
| QtdPes | Number(008,2) | Sim | Quantidade de Pessoas |
| UniCre | String(001) | Não | Unidade de Tempo do C. Recurso (D=Dias, H=Horas, M=Minutos, S=Segundos) |
| HorTrb | Number(004,2) | Não | Quantidade diária de horas trabalhadas no Centro de Recurso |
| CodCcu | String(009) | Sim | Código do Centro de Custo |
| CodLoc | String(024) | Sim | Código do Local Conforme Organograma da Empresa (Sistema Vetorh) |
| PerEfi | Number(005,2) | Sim | Percentual de eficiência de produção do centro de recurso |
| MovOrp | String(001) | Sim | Indica se C. Recurso gera movimentação de OPs por operação/operador (propõem valor p/ Roteiro) |
| CapSmt | Number(014,5) | Sim | Capacidade produtiva simultânea (por unidade de produto) |
| DesCpl | String(240) | Sim | Descrição Complementar do Centro de Recurso |
| CreCri | String(001) | Sim | Indica se C. Recurso é crítico ou não p/ avaliação de Capacidade |
| RecFra | String(001) | Sim | Indica se o C. Recursos pode ser considerado fracionado na Substituição de recursos da Carga |
| HorAlt | Number(005,0) | Sim | Hora da alteração do Registro |
| DatAlt | Date | Sim | Data da alteração do Registro |
| CodUsu | Number(010,0) | Sim | Código do usuário que alterou o Registro |
| VolCre | Number(011,5) | Sim | Volume do recurso |
| FenCre | Number(013,7) | Sim | Fator de enchimento do recurso |
| TmpPro | Number(009,0) | Sim | Tempo que o Centro de Recurso levará para produzir uma unidade do produto |
| TcrCus | Number(015,6) | Sim | Taxa real de custo do centro de recurso |
| IndOee | String(001) | Sim | Indica se centro de recurso deve ter indicadores para o painel OEE calculados |
| IndSer | String(001) | Sim | Indicativo de uso exclusivo para roteiro de OS |
| USU_codset | String(010) | Sim | Setor |
| USU_DefCre | Number(003,0) | Sim | Quantidade de Dias para Defasagem do Centro de Recurso |
| USU_FamCre | String(015) | Sim | Familia do Centro de Recurso |
| USU_ArqVar | String(050) | Sim | Arquivo/Varal |
| USU_PerFad | Number(005,2) | Sim | Percentual da fadiga no centro de recurso |
| USU_PerTu | Number(005,2) | Sim | Percentual do tempo de uso  no centro de recurso |
| USU_IndMan | String(001) | Sim | Indicador de manutenção do centro de recurso |
| USU_IndPin | String(001) | Sim | Passagem Pintura |
| USU_SitCre | String(001) | Sim | Situacao do Centro de Recurso |
| USU_FilPro | Number(005,0) | Sim | Filial de Produção do Recurso |

---

## Chave Primária

- CodEmp
- CodCre

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
