# E085CTO

## Descrição

Cadastros - Clientes - Contatos

---

## Resumo

- Campos: 42
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do Cliente |
| SeqCto | Number(005,0) | Não | Seqüência da pessoa de contato no cliente |
| NomCto | String(150) | Não | Nome da pessoa de contato |
| DatNas | Date | Sim | Data de nascimento da pessoa de contato |
| NivCto | String(001) | Sim | (descontinuado) Nível da pessoa de contato |
| SetCto | String(030) | Sim | Setor da pessoa de contato |
| CarCto | String(050) | Sim | Cargo da pessoa de contato |
| FonCto | String(020) | Sim | Número do 1º telefone da pessoa de contato |
| RamCto | Number(004,0) | Sim | Número do ramal da pessoa de contato (1º telefone) |
| FonCt2 | String(020) | Sim | Número do 2º telefone da pessoa de contato |
| RamCt2 | Number(004,0) | Sim | Número do ramal da pessoa de contato (2º telefone) |
| FonCt3 | String(020) | Sim | Número do 3º telefone da pessoa de contato |
| RamCt3 | Number(004,0) | Sim | Número do ramal da pessoa de contato (3º telefone) |
| FaxCto | String(020) | Sim | Número do FAX da pessoa de contato |
| IntNet | String(100) | Sim | Endereço eletrônico (E-Mail) da pessoa de contato |
| HobCon | String(015) | Sim | Hobby da pessoa de contato |
| TimCon | String(015) | Sim | Time da pessoa de contato |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palmtop |
| DatPal | Date | Sim | Data da última alteração para o palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o palmtop |
| SitCto | String(001) | Sim | Situação do registro |
| CodNiv | Number(004,0) | Sim | Código do Nível |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| EnvCre | String(001) | Sim | Forma de envio do receituário para o Sign |
| USU_clicat | Number(013,0) | Sim | Cliente catalogo |
| USU_seqcto | Number(004,0) | Sim | Sequencia |
| USU_comcom | String(001) | Sim | Comunicacao |
| USU_ZAPCON | String(020) | Sim | Whatsapp do Contato |
| USU_EndCto | String(200) | Sim | Endereço do Contato |
| USU_EndCom | String(200) | Sim | Complemento do Endereço |
| USU_CepCon | Number(008,0) | Sim | CEP do Contato |
| USU_UFsCon | String(002) | Sim | UF do Contato |
| USU_CidCon | String(200) | Sim | Cidade do Contato |
| USU_CelCto | String(020) | Sim | Celular do Contato |
| USU_CodPai | String(004) | Sim | Código do País |
| USU_NenCto | String(060) | Sim | Número do Endereço |
| USU_CtoPdr | String(001) | Sim | Contato Padrão |

---

## Chave Primária

- CodCli
- SeqCto

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E085CTO_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

