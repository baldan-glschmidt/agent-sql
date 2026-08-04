# E088CCL

## Descrição

Tabelas - Certificado de Classificação - Dados Gerais

---

## Resumo

- Campos: 48
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| SerCcl | String(003) | Não | Série do certificado de classificação |
| NumCcl | String(015) | Não | Número do certificado de classificação |
| RegMag | String(012) | Sim | Número do registro no ministério de agricultura |
| ProPro | String(060) | Sim | Cidade de procedência do produto |
| EstPro | String(002) | Sim | Estado de procedência do produto |
| NomDst | String(030) | Sim | Nome do destinatário do produto |
| CidDst | String(060) | Sim | Cidade do destinatário do produto |
| EstDst | String(002) | Sim | Estado do destinatário do produto |
| DesPro | String(040) | Sim | Descrição do produto |
| NumVol | Number(009,0) | Sim | Número do volume |
| NumLot | String(012) | Sim | Número do lote |
| NumSaf | String(012) | Sim | Número da safra |
| PesBru | Number(014,5) | Sim | Peso bruto do produto certificado |
| PesLiq | Number(014,5) | Sim | Peso líquido do produto certificado |
| VenBru | Number(014,5) | Sim | Peso bruto do produto vendido |
| VenLiq | Number(014,5) | Sim | Peso líquido do produto vendido |
| NotFis | Number(009,0) | Sim | Número da nota fiscal |
| SerNot | String(003) | Sim | Série da nota fiscal |
| EmbPro | String(020) | Sim | Embalagem do produto |
| MarPro | String(020) | Sim | Marca do produto |
| NotOpe | String(020) | Sim | Natureza de operação |
| GruPro | String(020) | Sim | Grupo do produto |
| SubGru | String(020) | Sim | Sub-grupo do produto |
| ClaPro | String(020) | Sim | Classe do produto |
| SubCla | String(020) | Sim | Sub-classe do produto |
| TipPro | String(020) | Sim | Tipo do produto |
| SubTip | String(020) | Sim | Sub-tipo do produto |
| CatPro | String(020) | Sim | Categoria do produto |
| SubCat | String(020) | Sim | Sub-categoria do produto |
| UmiPro | Number(005,2) | Sim | Percentual de umidade |
| PerRen | Number(005,2) | Sim | Percentual de renda do produto |
| PerRgi | Number(005,2) | Sim | Percentual de rendimento de grãos inteiros |
| PerRgo | Number(005,2) | Sim | Percentual de rendimento de grãos quebrados |
| LocCla | String(060) | Sim | Cidade ou Local de classificação |
| EstCla | String(002) | Sim | Estado do local de classificação |
| DatEmi | Date | Sim | Data de emissão do certificado de classificação |
| DatVal | Date | Sim | Data de validade do certificado de classificação |
| NomCla | String(100) | Sim | Nome do classificador |
| NumRma | String(012) | Sim | Número do registro do classificador no ministério da agricultura |
| ObsCcl | String(250) | Sim | Observação do certificado de classificação |
| SitReg | String(001) | Sim | Situação do registro |
| ObsSit | String(250) | Sim | Observação da situação do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| NomEmi | String(100) | Sim | Nome do responsável pela emissão do certificado. |
| NomClt | String(100) | Sim | Nome do Responsável pela Coleta |

---

## Chave Primária

- CodEmp
- SerCcl
- NumCcl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E088CCL_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

