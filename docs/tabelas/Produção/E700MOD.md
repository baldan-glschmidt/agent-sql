# E700MOD

## Descrição

Ficha - Modelo - Dados Gerais

---

## Resumo

- Campos: 30
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa. |
| CodMod | String(014) | Não | Código do Modelo associado ao Produto. |
| DesMod | String(100) | Sim | Descrição do Modelo |
| CodFam | String(006) | Não | Código da  Família de produto ao qual  o  Modelo pertence |
| QtdBas | Number(014,5) | Não | Quantidade base p/ compor proporcionalmente o consumo dos componentes |
| UniMed | String(003) | Não | Unidade de Medida da Família do Produto |
| CodMdp | String(008) | Não | Código da Máscara de Derivação permitida |
| CodClc | String(010) | Sim | Código da coleção do produto |
| CodClf | String(003) | Sim | Código interno da classificação fiscal do produto |
| FilPrd | Number(005,0) | Sim | Código da filial de produção do produto |
| QtdMax | Number(012,5) | Sim | Quantidade Máxima para uma Ordem produção/compra |
| CodAem | String(010) | Sim | Código do agrupamento para embalagens |
| CodAge | String(005) | Sim | Código de agrupamento de materiais/produtos para estoques |
| TolQmx | Number(005,3) | Sim | Tolerância da quantidade máxima defininida no produto |
| CodRot | String(014) | Sim | Código do Roteiro de Produção p/ Produto Fabricado |
| SitMod | String(001) | Não | Situação do Modelo (A=Ativo, I=Inativo) |
| DatGer | Date | Sim | Data da Geração do Modelo |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(010,0) | Sim | Código do usuário responsável pelo geração do registro |
| DatAlt | Date | Não | Data de Geração ou Alteração do Modelo p/ controle (Custos) |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(010,0) | Sim | Código do usuário responsável pelo alteração do registro |
| UsoCus | String(001) | Sim | Já foi utilizado p/ formação de preço de Custos? (S=Sim, N=Não) |
| VerMod | String(015) | Sim | Última versão do Modelo na qual e incrementada em cada nova alteração |
| RotAnx | Number(002,0) | Sim | Código da rotina para controle de arquivos anexos |
| NumAnx | Number(010,0) | Sim | Número do controle de arquivos anexos gerado pelo sistema |
| CodCre | String(008) | Sim | Código do Centro de Recurso (conjunto Máquina/Pessoa c/ mesma capacidade produtiva) |
| VolCre | Number(011,5) | Sim | Volume do recurso |
| FenCre | Number(013,7) | Sim | Fator de enchimento do recurso |
| IndFml | String(001) | Sim | Indicador que o modelo foi gerado pela tela de fórmulas |

---

## Chave Primária

- CodEmp
- CodMod

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E700MOD_003

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFam | CodFam |

### IR_E700MOD_005

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMed | UniMed |

### IR_E700MOD_006

**Tabela:** E084MDP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMdp | CodMdp |

