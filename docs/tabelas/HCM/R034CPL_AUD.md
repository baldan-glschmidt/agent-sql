# R034CPL_AUD

## Descrição

Auditoria Ficha Complementar

---

## Resumo

- Campos: 37
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(015,0) | Não | Sequencia do Registro |
| VerSeq | Number(010,0) | Não | Versão da Sequencia |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| CodPai | Number(004,0) | Sim | Código do País |
| CodEst | String(004) | Sim | Estado |
| CodCid | Number(007,0) | Sim | Cidade |
| CodBai | Number(004,0) | Sim | Bairro |
| EndCep | Number(008,0) | Sim | CEP |
| EndRua | String(100) | Sim | Endereço Residencial |
| EndNum | String(006) | Sim | Número |
| EndCpl | String(025) | Sim | Complemento Endereço |
| PaiNas | Number(004,0) | Sim | Código do País Nascimento |
| EstNas | String(004) | Sim | Estado Nascimento |
| CciNas | Number(007,0) | Sim | Cidade de Nascimento |
| NumCid | String(016) | Sim | Número da Carteira de Identidade |
| EmiCid | String(020) | Sim | Orgão Emissor da Carteira de Identidade |
| CidEmi | Number(007,0) | Sim | Cidade de Emissão do Documento |
| EstCid | String(002) | Sim | Estado do Orgão Emissor da Carteira de Identidade |
| DexCid | Date | Sim | Data de Expedição da Carteira de Identidade |
| EmaPar | String(100) | Sim | Endereço do Correio Eletrônico (E-mail) Particular |
| EmaCom | String(100) | Sim | Endereço do Correio Eletrônico (E-mail) Comercial |
| NumTel | String(020) | Sim | Número do Telefone |
| NumRam | String(015) | Sim | Número do Ramal |
| DddTel | Number(003,0) | Sim | Código DDD do Telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do Telefone |
| NumCnh | String(020) | Sim | Número da Carteira de Habilitação |
| CatCnh | String(004) | Sim | Categoria da Carteira de Habilitação |
| DatCnh | Date | Sim | Data da Expedição da CNH |
| VenCnh | Date | Sim | Data de Validade da Carteira de Habilitação |
| NumPsp | String(020) | Sim | Número do Passaporte |
| EmiPsp | String(006) | Sim | Emissor do Passaporte |
| EstPsp | String(004) | Sim | Estado do Passaporte |
| DemPsp | Date | Sim | Data de Emissão do Passaporte |
| DvaPsp | Date | Sim | Data de Validade do Passaporte |
| PaiPsp | Number(004,0) | Sim | País de emissão do Passaporte |

---

## Chave Primária

- SeqReg
- VerSeq
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
